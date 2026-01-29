from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.number_t import NumberT
from iodd_parser.generated.v1_1.uinteger_value_range_t import (
    UintegerValueRangeT,
)
from iodd_parser.generated.v1_1.uinteger_value_t import UintegerValueT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UintegerT(NumberT):
    class Meta:
        name = "UIntegerT"

    single_value: list[UintegerValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[UintegerValueRangeT] = field(
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
