from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.simple_datatype_t_2 import SimpleDatatypeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class OctetStringT2(SimpleDatatypeT2):
    class Meta:
        name = "OctetStringT"

    fixed_length: int | str = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
