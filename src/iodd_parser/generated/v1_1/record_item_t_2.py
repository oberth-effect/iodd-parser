from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t_2 import AccessRightsT2
from iodd_parser.generated.v1_1.datatype_ref_t_2 import DatatypeRefT2
from iodd_parser.generated.v1_1.simple_datatype_t_2 import SimpleDatatypeT2
from iodd_parser.generated.v1_1.text_ref_t_2 import TextRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class RecordItemT2:
    class Meta:
        name = "RecordItemT"

    simple_datatype: list[SimpleDatatypeT2] = field(
        default_factory=list,
        metadata={
            "name": "SimpleDatatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
    datatype_ref: list[DatatypeRefT2] = field(
        default_factory=list,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
    name: TextRefT2 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    description: None | TextRefT2 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    subindex: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    bit_offset: object = field(
        metadata={
            "name": "bitOffset",
            "type": "Attribute",
            "required": True,
        }
    )
    access_right_restriction: None | AccessRightsT2 = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
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
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )
