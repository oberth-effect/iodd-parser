from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.integer_value_range_t_2 import (
    IntegerValueRangeT2,
)
from iodd_parser.generated.v1_1.integer_value_t_2 import IntegerValueT2
from iodd_parser.generated.v1_1.number_t_2 import NumberT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class IntegerT2(NumberT2):
    class Meta:
        name = "IntegerT"

    single_value: list[IntegerValueT2] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[IntegerValueRangeT2] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
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
