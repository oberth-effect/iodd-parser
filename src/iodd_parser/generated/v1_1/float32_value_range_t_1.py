from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.value_range_t_1 import ValueRangeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class Float32ValueRangeT1(ValueRangeT1):
    class Meta:
        name = "Float32ValueRangeT"

    lower_value: float = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
        }
    )
    upper_value: float = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
        }
    )
