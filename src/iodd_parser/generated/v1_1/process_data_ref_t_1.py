from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.process_data_info_t_1 import ProcessDataInfoT1
from iodd_parser.generated.v1_1.process_data_record_item_info_t_1 import (
    ProcessDataRecordItemInfoT1,
)

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ProcessDataRefT1:
    class Meta:
        name = "ProcessDataRefT"

    process_data_info: list[ProcessDataInfoT1] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
    process_data_record_item_info: list[ProcessDataRecordItemInfoT1] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    process_data_id: str = field(
        metadata={
            "name": "processDataId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )
