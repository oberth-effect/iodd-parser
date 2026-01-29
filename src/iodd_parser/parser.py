import io
import zipfile
from dataclasses import dataclass
from importlib.resources import files
from importlib.resources.abc import Traversable
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser

from iodd_parser.generated.v1_1 import (
    IoddstandardDefinitions,
    IoddstandardUnitDefinitions,
    IoddstandardVariableT,
    Iodevice,
    StdVariableRefT,
    TextRefT,
    VariableCollectionT,
)

STANDARD_DEFINITIONS_PACKAGE = "iodd_parser.standard_definitions"
STANDARD_DEFINITIONS_VERSION = "v1_1"

IODD_IMAGE_FORMATS = {
    ".png",
}


@dataclass
class IoddImage:
    filename: str
    data: bytes


type Variable = VariableCollectionT.Variable | tuple[IoddstandardVariableT, StdVariableRefT]


@dataclass
class ParsedIODD:
    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice

    # variables: list[Variable]
    images: list[IoddImage]
    # texts: dict[str, str]

    def get_text(self, ref: TextRefT):
        pass


def _resolve_standard_definition_source(value: str | Path) -> Path | Traversable:
    if isinstance(value, Path):
        return value

    if isinstance(value, str):
        resource_dir = files(STANDARD_DEFINITIONS_PACKAGE).joinpath(STANDARD_DEFINITIONS_VERSION)
        file_path = Path(value)
        if len(file_path.parts) == 1:
            candidate = resource_dir.joinpath(file_path.name)
            if candidate.is_file():
                return candidate
        return file_path

    raise TypeError(f"Unsupported standard definition type: {type(value)!r}")


class IODDParser:
    load_images: bool

    _loaded_definitions: IoddstandardDefinitions
    _loaded_units: IoddstandardUnitDefinitions

    def __init__(
        self,
        standard_definitions: str | Path = "IODD-StandardDefinitions1.1.xml",
        standard_unit_definitions: str | Path = "IODD-StandardUnitDefinitions1.1.xml",
        load_images: bool = False,
    ):
        self.load_images = load_images

        parser = XmlParser()

        definitions_source = _resolve_standard_definition_source(standard_definitions)
        units_source = _resolve_standard_definition_source(standard_unit_definitions)

        self._loaded_definitions = parser.parse(definitions_source, IoddstandardDefinitions)
        self._loaded_units = parser.parse(units_source, IoddstandardUnitDefinitions)

    def parse(self, zip_path: str | Path, lang=None):
        zip_pth = Path(zip_path)
        if not zip_pth.is_file():
            raise FileNotFoundError(f"IODD zip not found: {zip_pth.resolve()}")

        xml_suffix = f"-IODD1.1-{lang}.xml" if lang else "-IODD1.1.xml"

        with zipfile.ZipFile(zip_pth, "r") as archive:
            xml_suffix_lower = xml_suffix.lower()
            xml_candidates = [
                name
                for name in archive.namelist()
                if not name.endswith("/") and name.lower().endswith(xml_suffix_lower)
            ]

            if not xml_candidates:
                raise FileNotFoundError(f"Expected IODD XML with suffix '{xml_suffix}' not found in {zip_pth.name}")
            if len(xml_candidates) > 1:
                raise ValueError(f"Multiple IODD XML files with suffix '{xml_suffix}' found: {xml_candidates}")

            xml_data = archive.read(xml_candidates[0])
            device = XmlParser().parse(io.BytesIO(xml_data), Iodevice)

            images: list[IoddImage] = []
            if self.load_images:
                for name in archive.namelist():
                    if name.endswith("/"):
                        continue
                    if Path(name).suffix.lower() in IODD_IMAGE_FORMATS:
                        images.append(IoddImage(filename=name, data=archive.read(name)))

        return ParsedIODD(self._loaded_definitions, self._loaded_units, device, images)

    @property
    def standard_definitions(self):
        return self._loaded_definitions

    @property
    def standard_definition_units(self):
        return self._loaded_units
