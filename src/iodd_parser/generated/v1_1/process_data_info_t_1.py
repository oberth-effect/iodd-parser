from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from iodd_parser.generated.v1_1.context_constraints_t import (
    ContextConstraintsT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ProcessDataInfoT1:
    class Meta:
        name = "ProcessDataInfoT"

    gradient: None | Decimal | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    offset: None | Decimal | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    unit_code: None | int | str = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    display_format: None | object = field(
        default=None,
        metadata={
            "name": "displayFormat",
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
