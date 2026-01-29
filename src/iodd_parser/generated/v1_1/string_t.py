from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.character_encoding_t import CharacterEncodingT
from iodd_parser.generated.v1_1.simple_datatype_t import SimpleDatatypeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StringT(SimpleDatatypeT):
    fixed_length: int = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
        }
    )
    encoding: CharacterEncodingT = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
