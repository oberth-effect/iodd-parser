from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_ref_t_2 import DatatypeRefT2
from iodd_parser.generated.v1_1.datatype_t_2 import DatatypeT2
from iodd_parser.generated.v1_1.object_t_2 import ObjectT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class DataItemT1(ObjectT2):
    class Meta:
        name = "DataItemT"

    datatype: None | DatatypeT2 = field(
        default=None,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    datatype_ref: None | DatatypeRefT2 = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
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
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )
