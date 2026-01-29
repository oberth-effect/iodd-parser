from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.std_data_item_ref_t_2 import StdDataItemRefT2
from iodd_parser.generated.v1_1.std_record_item_ref_t_2 import (
    StdRecordItemRefT2,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StdVariableRefT2(StdDataItemRefT2):
    class Meta:
        name = "StdVariableRefT"

    std_record_item_ref: list[StdRecordItemRefT2] = field(
        default_factory=list,
        metadata={
            "name": "StdRecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    fixed_length_restriction: None | int = field(
        default=None,
        metadata={
            "name": "fixedLengthRestriction",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )
