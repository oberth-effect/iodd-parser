from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.character_encoding_t_1 import (
    CharacterEncodingT1,
)
from iodd_parser.generated.v1_1.simple_datatype_t_1 import SimpleDatatypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StringT1(SimpleDatatypeT1):
    class Meta:
        name = "StringT"

    fixed_length: int = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
        }
    )
    encoding: CharacterEncodingT1 = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
