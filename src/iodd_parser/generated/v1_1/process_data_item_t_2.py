from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.data_item_t_2 import DataItemT2
from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataItemT2(DataItemT2):
    class Meta:
        name = "ProcessDataItemT"

    name: TextRefT1 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 256,
        }
    )
