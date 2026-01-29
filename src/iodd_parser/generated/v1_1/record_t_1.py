from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.complex_datatype_t_1 import ComplexDatatypeT1
from iodd_parser.generated.v1_1.record_item_t_1 import RecordItemT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class RecordT1(ComplexDatatypeT1):
    class Meta:
        name = "RecordT"

    record_item: list[RecordItemT1] = field(
        default_factory=list,
        metadata={
            "name": "RecordItem",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 1856,
        }
    )
