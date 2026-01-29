from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.std_data_item_ref_t_1 import StdDataItemRefT1
from iodd_parser.generated.v1_1.std_record_item_ref_t_1 import (
    StdRecordItemRefT1,
)

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class StdVariableRefT1(StdDataItemRefT1):
    class Meta:
        name = "StdVariableRefT"

    std_record_item_ref: list[StdRecordItemRefT1] = field(
        default_factory=list,
        metadata={
            "name": "StdRecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    fixed_length_restriction: None | int | str = field(
        default=None,
        metadata={
            "name": "fixedLengthRestriction",
            "type": "Attribute",
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )
