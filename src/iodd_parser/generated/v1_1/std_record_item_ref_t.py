from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.std_data_item_ref_t import StdDataItemRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StdRecordItemRefT(StdDataItemRefT):
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
