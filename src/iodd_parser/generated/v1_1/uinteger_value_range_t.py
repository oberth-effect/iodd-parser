from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.value_range_t import ValueRangeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UintegerValueRangeT(ValueRangeT):
    class Meta:
        name = "UIntegerValueRangeT"

    lower_value: int = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
        }
    )
    upper_value: int = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
        }
    )
