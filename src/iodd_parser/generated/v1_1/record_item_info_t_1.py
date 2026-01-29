from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class RecordItemInfoT1:
    class Meta:
        name = "RecordItemInfoT"

    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
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
