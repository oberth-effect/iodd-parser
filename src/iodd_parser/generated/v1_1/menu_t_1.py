from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.context_constraints_t import (
    ContextConstraintsT,
)
from iodd_parser.generated.v1_1.text_ref_t_2 import TextRefT2
from iodd_parser.generated.v1_1.uimenu_ref_t_1 import UimenuRefT1
from iodd_parser.generated.v1_1.uirecord_item_ref_t_1 import UirecordItemRefT1
from iodd_parser.generated.v1_1.uivariable_ref_t_1 import UivariableRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class MenuT1:
    class Meta:
        name = "MenuT"

    name: None | TextRefT2 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable_ref: list[UivariableRefT1] = field(
        default_factory=list,
        metadata={
            "name": "VariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    record_item_ref: list[UirecordItemRefT1] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    menu_ref: list[UimenuRefT1] = field(
        default_factory=list,
        metadata={
            "name": "MenuRef",
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
    context_constraints: None | ContextConstraintsT = field(
        default=None,
        metadata={
            "name": "contextConstraints",
            "type": "Attribute",
        },
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
