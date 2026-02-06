"""
IODD Parser module.

This module provides the [`iodd_parser.IODDParser`][] class for parsing IO-Link
Device Description (IODD) files packaged as ZIP archives.
"""

import io
import zipfile
from importlib.resources import files
from importlib.resources.abc import Traversable
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser

from iodd_parser.generated.v1_1 import (
    ExternalTextDocument,
    IoddstandardDefinitions,
    IoddstandardUnitDefinitions,
    Iodevice,
)
from iodd_parser.types import (
    IoddImage,
    ParsedIODD,
    ResolvedIODD,
)

STANDARD_DEFINITIONS_PACKAGE = "iodd_parser.standard_definitions"
STANDARD_DEFINITIONS_VERSION = "v1_1"

IODD_IMAGE_FORMATS = {
    ".png",
}


def _get_bundled_resource(filename: str) -> Traversable:
    """
    Get a file from the bundled standard definitions package.

    :param filename: Name of the file to retrieve.
    :returns: Traversable resource for the file.
    """
    return files(STANDARD_DEFINITIONS_PACKAGE).joinpath(STANDARD_DEFINITIONS_VERSION, filename)


class IODDParser:
    """
    Parser for IO-Link Device Description (IODD) files.

    This class parses IODD ZIP archives and resolves all references to
    produce a unified [`iodd_parser.ParsedIODD`][] result with resolved text strings,
    datatypes, variables, errors, units, and process data.

    :param standard_definitions_folder: Optional path to a folder containing
        standard definitions and language files. When provided, all files are
        loaded from this folder and all language files matching the pattern
        ``<base>-<lang>.xml`` are auto-discovered.
    :param standard_definitions_filename: Filename of the standard definitions XML.
        Defaults to IODD-StandardDefinitions1.1.xml.
    :param standard_unit_filename: Filename of the standard unit definitions XML.
        Defaults to IODD-StandardUnitDefinitions1.1.xml.
    :param load_images: Whether to extract and load images from the IODD archive.
        Defaults to False.

    Example usage::

        parser = IODDParser()

        # Two-step: parse then resolve
        parsed = parser.parse("device.zip")
        print(f"Available languages: {parsed.available_languages}")
        result = parsed.resolve(lang="de")

        # Or one-step convenience method
        result = parser.parse_and_resolve("device.zip", lang="de")

        print(result.device_name)
        for var_id, var in result.variables.items():
            print(f"{var_id}: {var.name}")

        # With a custom folder containing standard definitions:
        parser = IODDParser(standard_definitions_folder="/path/to/definitions")
    """

    load_images: bool
    _loaded_definitions: IoddstandardDefinitions
    _loaded_units: IoddstandardUnitDefinitions
    _lang_texts: dict[str, dict[str, str]]

    def __init__(
        self,
        standard_definitions_folder: str | Path | None = None,
        standard_definitions_filename: str = "IODD-StandardDefinitions1.1.xml",
        standard_unit_filename: str = "IODD-StandardUnitDefinitions1.1.xml",
        load_images: bool = False,
    ):
        self.load_images = load_images

        parser = XmlParser()

        # Determine sources based on whether a folder is provided
        if standard_definitions_folder is not None:
            folder = Path(standard_definitions_folder)
            definitions_source = folder / standard_definitions_filename
            units_source = folder / standard_unit_filename
        else:
            definitions_source = _get_bundled_resource(standard_definitions_filename)
            units_source = _get_bundled_resource(standard_unit_filename)

        self._loaded_definitions = parser.parse(definitions_source, IoddstandardDefinitions)
        self._loaded_units = parser.parse(units_source, IoddstandardUnitDefinitions)

        # Pre-load language-specific standard definitions (texts only)
        self._lang_texts = {}
        def_base = Path(standard_definitions_filename)
        base_stem = def_base.stem
        lang_prefix = f"{base_stem}-"

        # Get iterable of (name, source) tuples for language file discovery
        if standard_definitions_folder is not None:
            folder = Path(standard_definitions_folder)
            lang_files = ((f.name, f) for f in folder.glob(f"{base_stem}-*{def_base.suffix}"))
        else:
            resource_dir = files(STANDARD_DEFINITIONS_PACKAGE).joinpath(STANDARD_DEFINITIONS_VERSION)
            lang_files = ((r.name, r) for r in resource_dir.iterdir() if r.is_file())

        for name, source in lang_files:
            stem = Path(name).stem
            if stem.startswith(lang_prefix):
                lang_code = stem[len(lang_prefix) :]
                if lang_code:
                    try:
                        lang_def = parser.parse(source, ExternalTextDocument)
                        self._lang_texts[lang_code] = {t.id: t.value for t in lang_def.language.text}
                    except (FileNotFoundError, OSError):
                        pass

    def parse(self, zip_path: str | Path) -> ParsedIODD:
        """
        Parse an IODD ZIP archive without resolving references.

        This method parses the XML files and discovers all available language files,
        returning a [`iodd_parser.ParsedIODD`][] object. Call
        [`ParsedIODD.resolve`][iodd_parser.ParsedIODD.resolve] on the result to resolve all
        references with an optional language.

        :param zip_path: Path to the IODD ZIP file.
        :returns: A [`iodd_parser.ParsedIODD`][] object with parsed XML data.
        :raises FileNotFoundError: If the ZIP file or expected XML is not found.
        :raises ValueError: If multiple matching XML files are found in the archive.
        """
        zip_pth = Path(zip_path)
        if not zip_pth.is_file():
            raise FileNotFoundError(f"IODD zip not found: {zip_pth.resolve()}")

        # Always look for the main IODD file (not language-specific)
        xml_suffix = "-IODD1.1.xml"
        xml_suffix_lower = xml_suffix.lower()

        with zipfile.ZipFile(zip_pth, "r") as archive:
            xml_candidates = [
                name
                for name in archive.namelist()
                if not name.endswith("/") and name.lower().endswith(xml_suffix_lower)
            ]

            if not xml_candidates:
                raise FileNotFoundError(f"Expected IODD XML with suffix '{xml_suffix}' not found in {zip_pth.name}")
            if len(xml_candidates) > 1:
                raise ValueError(f"Multiple IODD XML files with suffix '{xml_suffix}' found: {xml_candidates}")

            main_xml_name = xml_candidates[0]
            xml_data = archive.read(main_xml_name)
            device = XmlParser().parse(io.BytesIO(xml_data), Iodevice)

            # Discover all language files in the archive
            # Language file pattern: <main_name_without_extension>-<lang>.xml
            device_lang_texts: dict[str, dict[str, str]] = {}
            main_base = main_xml_name.rsplit(".", 1)[0]  # Remove .xml extension
            lang_prefix = f"{main_base}-".lower()

            for name in archive.namelist():
                if name.endswith("/"):
                    continue
                name_lower = name.lower()
                if name_lower.startswith(lang_prefix) and name_lower.endswith(".xml"):
                    # Extract language code from filename
                    # e.g., "VendorX-DeviceY-20110603-IODD1.1-de.xml" -> "de"
                    lang_part = name[len(main_base) + 1 : -4]  # Remove prefix and .xml
                    if lang_part and "-" not in lang_part:  # Valid language code (no extra dashes)
                        try:
                            lang_xml_data = archive.read(name)
                            lang_doc = XmlParser().parse(io.BytesIO(lang_xml_data), ExternalTextDocument)
                            device_lang_texts[lang_part] = {t.id: t.value for t in lang_doc.language.text}
                        except (OSError, Exception):
                            pass  # Skip invalid language files

            images: list[IoddImage] = []
            if self.load_images:
                for name in archive.namelist():
                    if name.endswith("/"):
                        continue
                    if Path(name).suffix.lower() in IODD_IMAGE_FORMATS:
                        images.append(IoddImage(filename=name, data=archive.read(name)))

        return ParsedIODD(
            iodd_definitions=self._loaded_definitions,
            iodd_units=self._loaded_units,
            iodd_device=device,
            standard_lang_texts=self._lang_texts,
            device_lang_texts=device_lang_texts,
            images=images,
        )

    def parse_and_resolve(self, zip_path: str | Path, lang: str | None = None) -> ResolvedIODD:
        """
        Parse an IODD ZIP archive and resolve all references.

        This is a convenience method that calls [`IODDParser.parse`][iodd_parser.IODDParser.parse]
        followed by [`ParsedIODD.resolve`][iodd_parser.ParsedIODD.resolve].

        :param zip_path: Path to the IODD ZIP file.
        :param lang: Optional language code (e.g., "de", "fr") for localised texts.
            When specified, texts are resolved in the following priority order
            (later sources override earlier ones):

            1. Primary language (English) from standard definitions
            2. Primary language from device IODD
            3. Primary language from standard unit definitions (English only)
            4. Pre-loaded language-specific standard definitions file (if available)
            5. Language sections within main standard definitions file
            6. Language sections within main device IODD file
            7. Device-specific language file (e.g., ``*-IODD1.1-de.xml``) - highest priority

        :returns: A [`iodd_parser.ResolvedIODD`][] object with all resolved data.
        :raises FileNotFoundError: If the ZIP file or expected XML is not found.
        :raises ValueError: If multiple matching XML files are found in the archive.
        """
        return self.parse(zip_path).resolve(lang)

    @property
    def standard_definitions(self) -> IoddstandardDefinitions:
        """
        Get the loaded standard definitions.

        :returns: The parsed standard definitions object.
        """
        return self._loaded_definitions

    @property
    def standard_definition_units(self) -> IoddstandardUnitDefinitions:
        """
        Get the loaded standard unit definitions.

        :returns: The parsed standard unit definitions object.
        """
        return self._loaded_units

    @property
    def language_texts(self) -> dict[str, dict[str, str]]:
        """
        Get the pre-loaded language-specific texts from standard definitions.

        :returns: A dictionary mapping language codes to their text dictionaries.
            Each text dictionary maps text IDs to their localised string values.
        """
        return self._lang_texts
