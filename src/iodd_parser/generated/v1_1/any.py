from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.number_t_2 import NumberT2
from iodd_parser.generated.v1_1.tbd_value_range_t import TbdValueRangeT
from iodd_parser.generated.v1_1.tbd_value_t import TbdValueT

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class AnyType(NumberT2):
    class Meta:
        name = "any"

    single_value: list[TbdValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[TbdValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    bit_length: None | int = field(
        default=None,
        metadata={
            "name": "bitLength",
            "type": "Attribute",
        },
    )
