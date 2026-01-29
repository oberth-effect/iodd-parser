from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.value_range_t_2 import ValueRangeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class Float32ValueRangeT2(ValueRangeT2):
    class Meta:
        name = "Float32ValueRangeT"

    lower_value: float | str = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    upper_value: float | str = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
