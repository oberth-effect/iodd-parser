"""
IODD Parser module.

This module provides the :class:`IODDParser` class for parsing IO-Link
Device Description (IODD) files packaged as ZIP archives.
"""

import io
import zipfile
from importlib.resources import files
from importlib.resources.abc import Traversable
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser

from iodd_parser.generated.v1_1 import (
    DatatypeT,
    ExternalTextDocument,
    IoddstandardDefinitions,
    IoddstandardUnitDefinitions,
    Iodevice,
    LanguageT,
)
from iodd_parser.resolvers import (
    resolve_errors,
    resolve_process_data,
    resolve_units,
    resolve_variables,
)
from iodd_parser.types import (
    IoddImage,
    ParsedIODD,
    ResolvedError,
    ResolvedProcessData,
    ResolvedProcessDataItem,
    ResolvedUnit,
    ResolvedVariable,
)

__all__ = [
    "IODDParser",
    "IoddImage",
    "ParsedIODD",
    "ResolvedError",
    "ResolvedProcessData",
    "ResolvedProcessDataItem",
    "ResolvedUnit",
    "ResolvedVariable",
]

STANDARD_DEFINITIONS_PACKAGE = "iodd_parser.standard_definitions"
STANDARD_DEFINITIONS_VERSION = "v1_1"

IODD_IMAGE_FORMATS = {
    ".png",
}


def _lang_id(lng: LanguageT) -> str:
    """
    Extract the language identifier from a LanguageT object.

    :param lng: The language object.
    :returns: The language identifier string.
    """
    if isinstance(lng.lang, str):
        return lng.lang
    return lng.lang.value


def _resolve_standard_definition_source(value: str | Path) -> Path | Traversable:
    """
    Resolve a standard definition file path.

    If a simple filename is provided, looks for it in the bundled
    standard definitions package. Otherwise, treats it as a filesystem path.

    :param value: Filename or path to the standard definition file.
    :returns: Resolved path or traversable resource.
    :raises TypeError: If the value type is not supported.
    """
    if isinstance(value, Path):
        return value

    if isinstance(value, str):
        resource_dir = files(STANDARD_DEFINITIONS_PACKAGE).joinpath(
            STANDARD_DEFINITIONS_VERSION
        )
        file_path = Path(value)
        if len(file_path.parts) == 1:
            candidate = resource_dir.joinpath(file_path.name)
            if candidate.is_file():
                return candidate
        return file_path

    raise TypeError(f"Unsupported standard definition type: {type(value)!r}")


class IODDParser:
    """
    Parser for IO-Link Device Description (IODD) files.

    This class parses IODD ZIP archives and resolves all references to
    produce a unified :class:`ParsedIODD` result with resolved text strings,
    datatypes, variables, errors, units, and process data.

    :param standard_definitions: Path or filename of the standard definitions XML.
        Defaults to the bundled IODD-StandardDefinitions1.1.xml.
    :param standard_unit_definitions: Path or filename of the standard unit
        definitions XML. Defaults to the bundled IODD-StandardUnitDefinitions1.1.xml.
    :param load_images: Whether to extract and load images from the IODD archive.
        Defaults to False.
    :param langs: Optional list of language codes (e.g., ["de", "fr"]) to pre-load
        from standard definitions. Language-specific files are loaded with the
        corresponding suffix (e.g., IODD-StandardDefinitions1.1-de.xml). Note that
        unit definitions only exist in English.

    Example usage::

        parser = IODDParser(langs=["de", "fr"])
        result = parser.parse("device.zip", lang="de")
        print(result.device_name)
        for var_id, var in result.variables.items():
            print(f"{var_id}: {var.name}")
    """

    load_images: bool
    _loaded_definitions: IoddstandardDefinitions
    _loaded_units: IoddstandardUnitDefinitions
    _lang_texts: dict[str, dict[str, str]]

    def __init__(
        self,
        standard_definitions: str | Path = "IODD-StandardDefinitions1.1.xml",
        standard_unit_definitions: str | Path = "IODD-StandardUnitDefinitions1.1.xml",
        load_images: bool = False,
        langs: list[str] | None = None,
    ):
        self.load_images = load_images

        parser = XmlParser()

        definitions_source = _resolve_standard_definition_source(standard_definitions)
        units_source = _resolve_standard_definition_source(standard_unit_definitions)

        self._loaded_definitions = parser.parse(
            definitions_source, IoddstandardDefinitions
        )
        self._loaded_units = parser.parse(units_source, IoddstandardUnitDefinitions)

        # Pre-load language-specific standard definitions (texts only)
        self._lang_texts = {}

        if langs:
            # Derive language-specific filenames from the base filename
            # Note: Only standard definitions have language files, not unit definitions
            def_base = Path(standard_definitions)

            for lang_code in langs:
                # Build language-specific filename: name-lang.xml
                def_lang_name = f"{def_base.stem}-{lang_code}{def_base.suffix}"

                try:
                    def_lang_source = _resolve_standard_definition_source(def_lang_name)
                    lang_def = parser.parse(def_lang_source, ExternalTextDocument)
                    self._lang_texts[lang_code] = {
                        t.id: t.value for t in lang_def.language.text
                    }
                except (FileNotFoundError, OSError):
                    pass  # Language file not available


    def parse(self, zip_path: str | Path, lang: str | None = None) -> ParsedIODD:
        """
        Parse an IODD ZIP archive.

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

            For standard definition language support, ensure the parser was initialised
            with the required languages via the ``langs`` parameter.
        :returns: A :class:`ParsedIODD` object with all resolved data.
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
                raise FileNotFoundError(
                    f"Expected IODD XML with suffix '{xml_suffix}' "
                    f"not found in {zip_pth.name}"
                )
            if len(xml_candidates) > 1:
                raise ValueError(
                    f"Multiple IODD XML files with suffix '{xml_suffix}' "
                    f"found: {xml_candidates}"
                )

            main_xml_name = xml_candidates[0]
            xml_data = archive.read(main_xml_name)
            device = XmlParser().parse(io.BytesIO(xml_data), Iodevice)

            # If language is requested, try to load the language file as ExternalTextDocument
            # Language file name: <main_name_without_extension>-<lang>.xml
            device_lang_texts: dict[str, str] = {}
            if lang:
                # Derive language file name from main file name
                # e.g., "VendorX-DeviceY-20110603-IODD1.1.xml" -> "VendorX-DeviceY-20110603-IODD1.1-ru.xml"
                main_base = main_xml_name.rsplit(".", 1)[0]  # Remove .xml extension
                lang_file_name = f"{main_base}-{lang}.xml"
                lang_file_name_lower = lang_file_name.lower()

                # Find the language file in the archive (case-insensitive)
                lang_file_match = next(
                    (
                        name
                        for name in archive.namelist()
                        if name.lower() == lang_file_name_lower
                    ),
                    None,
                )

                if lang_file_match:
                    lang_xml_data = archive.read(lang_file_match)
                    lang_doc = XmlParser().parse(
                        io.BytesIO(lang_xml_data), ExternalTextDocument
                    )
                    device_lang_texts = {
                        t.id: t.value for t in lang_doc.language.text
                    }

            images: list[IoddImage] = []
            if self.load_images:
                for name in archive.namelist():
                    if name.endswith("/"):
                        continue
                    if Path(name).suffix.lower() in IODD_IMAGE_FORMATS:
                        images.append(
                            IoddImage(filename=name, data=archive.read(name))
                        )

        # Resolve text collections with language support
        # Always start with the primary language (English) as base
        texts: dict[str, str] = {
            t.id: t.value
            for t in self._loaded_definitions.external_text_collection.primary_language.text
        }
        texts.update({
            t.id: t.value
            for t in device.external_text_collection.primary_language.text
        })
        texts.update({
            t.id: t.value
            for t in self._loaded_units.external_text_collection.primary_language.text
        })

        # If a specific language is requested, overlay those texts on top
        if lang:
            # First, apply pre-loaded language-specific standard definitions texts
            if lang in self._lang_texts:
                texts.update(self._lang_texts[lang])

            # Also check for language sections within the main definitions file (fallback)
            lang_dfs = next(
                (
                    x
                    for x in self._loaded_definitions.external_text_collection.language
                    if _lang_id(x) == lang
                ),
                None,
            )
            if lang_dfs is not None:
                texts.update({t.id: t.value for t in lang_dfs.text})

            # Check for language sections within the main device IODD file
            lang_dev = next(
                (
                    x
                    for x in device.external_text_collection.language
                    if _lang_id(x) == lang
                ),
                None,
            )
            if lang_dev is not None:
                texts.update({t.id: t.value for t in lang_dev.text})

            # Finally, overlay device-specific language file texts (highest priority)
            if device_lang_texts:
                texts.update(device_lang_texts)


        # Build datatypes lookup from both standard definitions and device
        datatypes: dict[str, DatatypeT] = {}
        if self._loaded_definitions.datatype_collection is not None:
            for dt in self._loaded_definitions.datatype_collection.datatype:
                if dt.id is not None:
                    datatypes[dt.id] = dt
        if device.profile_body.device_function.datatype_collection is not None:
            for dt in device.profile_body.device_function.datatype_collection.datatype:
                if dt.id is not None:
                    datatypes[dt.id] = dt

        # Resolve all collections
        errors = resolve_errors(
            self._loaded_definitions.error_type_collection,
            device.profile_body.device_function.error_type_collection,
            texts,
        )

        units = resolve_units(self._loaded_units, texts)

        variables = resolve_variables(
            self._loaded_definitions.variable_collection,
            device.profile_body.device_function.variable_collection,
            texts,
            datatypes,
        )

        process_data = resolve_process_data(
            device.profile_body.device_function.process_data_collection,
            texts,
            datatypes,
        )

        # Extract device identity information
        device_identity = device.profile_body.device_identity
        device_name = texts.get(
            device_identity.device_name.text_id,
            device_identity.device_name.text_id,
        )

        return ParsedIODD(
            iodd_definitions=self._loaded_definitions,
            iodd_units=self._loaded_units,
            iodd_device=device,
            device_name=device_name,
            device_manufacturer=device_identity.vendor_name,
            variables=variables,
            process_data=process_data,
            texts=texts,
            datatypes=datatypes,
            errors=errors,
            units=units,
            images=images,
        )

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
