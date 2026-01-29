from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.float32_value_range_t import Float32ValueRangeT
from iodd_parser.generated.v1_1.float32_value_t import Float32ValueT
from iodd_parser.generated.v1_1.number_t import NumberT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class Float32T(NumberT):
    single_value: list[Float32ValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[Float32ValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
