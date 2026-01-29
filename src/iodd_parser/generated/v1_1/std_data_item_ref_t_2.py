from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.single_value_t_1 import SingleValueT1
from iodd_parser.generated.v1_1.std_single_value_ref_t_2 import (
    StdSingleValueRefT2,
)
from iodd_parser.generated.v1_1.value_range_t_1 import ValueRangeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StdDataItemRefT2:
    class Meta:
        name = "StdDataItemRefT"

    std_single_value_ref: list[StdSingleValueRefT2] = field(
        default_factory=list,
        metadata={
            "name": "StdSingleValueRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    single_value: list[StdDataItemRefT2.SingleValue] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[StdDataItemRefT2.ValueRange] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class SingleValue(SingleValueT1):
        value: object = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ValueRange(ValueRangeT1):
        lower_value: object = field(
            metadata={
                "name": "lowerValue",
                "type": "Attribute",
                "required": True,
            }
        )
        upper_value: object = field(
            metadata={
                "name": "upperValue",
                "type": "Attribute",
                "required": True,
            }
        )
