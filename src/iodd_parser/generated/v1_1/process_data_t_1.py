from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.condition_t_2 import ConditionT2
from iodd_parser.generated.v1_1.object_t_2 import ObjectT2
from iodd_parser.generated.v1_1.process_data_item_t_1 import ProcessDataItemT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ProcessDataT1(ObjectT2):
    class Meta:
        name = "ProcessDataT"

    condition: None | ConditionT2 = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    process_data_in: list[ProcessDataItemT1] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataIn",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    process_data_out: list[ProcessDataItemT1] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataOut",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
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
