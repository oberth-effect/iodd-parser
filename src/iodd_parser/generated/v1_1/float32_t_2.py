from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.float32_value_range_t_2 import (
    Float32ValueRangeT2,
)
from iodd_parser.generated.v1_1.float32_value_t_2 import Float32ValueT2
from iodd_parser.generated.v1_1.number_t_2 import NumberT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class Float32T2(NumberT2):
    class Meta:
        name = "Float32T"

    single_value: list[Float32ValueT2] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[Float32ValueRangeT2] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
