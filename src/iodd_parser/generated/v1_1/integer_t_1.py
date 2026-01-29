from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.integer_value_range_t_1 import (
    IntegerValueRangeT1,
)
from iodd_parser.generated.v1_1.integer_value_t_1 import IntegerValueT1
from iodd_parser.generated.v1_1.number_t_1 import NumberT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IntegerT1(NumberT1):
    class Meta:
        name = "IntegerT"

    single_value: list[IntegerValueT1] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[IntegerValueRangeT1] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 64,
        }
    )
