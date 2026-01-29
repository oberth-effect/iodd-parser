from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.float32_value_range_t_1 import (
    Float32ValueRangeT1,
)
from iodd_parser.generated.v1_1.float32_value_t_1 import Float32ValueT1
from iodd_parser.generated.v1_1.number_t_1 import NumberT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class Float32T1(NumberT1):
    class Meta:
        name = "Float32T"

    single_value: list[Float32ValueT1] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[Float32ValueRangeT1] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
