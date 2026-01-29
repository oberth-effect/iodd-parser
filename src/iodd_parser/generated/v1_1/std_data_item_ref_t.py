from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.single_value_t import SingleValueT
from iodd_parser.generated.v1_1.std_single_value_ref_t import (
    StdSingleValueRefT,
)
from iodd_parser.generated.v1_1.value_range_t import ValueRangeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StdDataItemRefT:
    std_single_value_ref: list[StdSingleValueRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdSingleValueRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    single_value: list[StdDataItemRefT.SingleValue] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[StdDataItemRefT.ValueRange] = field(
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
    class SingleValue(SingleValueT):
        value: object = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ValueRange(ValueRangeT):
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
