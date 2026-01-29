from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.complex_datatype_t_2 import ComplexDatatypeT2
from iodd_parser.generated.v1_1.record_item_t_2 import RecordItemT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class RecordT2(ComplexDatatypeT2):
    class Meta:
        name = "RecordT"

    record_item: list[RecordItemT2] = field(
        default_factory=list,
        metadata={
            "name": "RecordItem",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
    bit_length: object = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
        }
    )
