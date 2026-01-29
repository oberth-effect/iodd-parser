from dataclasses import dataclass

from xsdata.formats.dataclass.parsers import XmlParser

from iodd_parser.generated.v1_1 import IoddstandardDefinitions, IoddstandardUnitDefinitions, Iodevice


@dataclass
class IoddImage:
    filename: str
    data: bytes

@dataclass
class Variable:
    id: str
    None | DatatypeT1


@dataclass
class ParsedIODD:
    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice


class IODDParser:
    load_images: bool

    _loaded_definitions: IoddstandardDefinitions
    _loaded_units: IoddstandardUnitDefinitions

    def __init__(self, standard_definitions, standard_unit_definitions, load_images: bool = False):
        self.load_images = load_images

        parser = XmlParser()
        self._loaded_definitions = parser.parse(standard_definitions, IoddstandardDefinitions)
        self._loaded_units = parser.parse(standard_unit_definitions, IoddstandardUnitDefinitions)

    def parse(self, zip_path):
        xml = ...
        return XmlParser().parse(xml, Iodevice)
