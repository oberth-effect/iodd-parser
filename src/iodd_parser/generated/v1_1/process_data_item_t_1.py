from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.data_item_t_1 import DataItemT1
from iodd_parser.generated.v1_1.text_ref_t_2 import TextRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ProcessDataItemT1(DataItemT1):
    class Meta:
        name = "ProcessDataItemT"

    name: TextRefT2 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    bit_length: object = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
        }
    )
