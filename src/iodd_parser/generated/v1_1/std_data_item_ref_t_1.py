from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.single_value_t_2 import SingleValueT2
from iodd_parser.generated.v1_1.std_single_value_ref_t_1 import (
    StdSingleValueRefT1,
)
from iodd_parser.generated.v1_1.value_range_t_2 import ValueRangeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class StdDataItemRefT1:
    class Meta:
        name = "StdDataItemRefT"

    std_single_value_ref: list[StdSingleValueRefT1] = field(
        default_factory=list,
        metadata={
            "name": "StdSingleValueRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    single_value: list[StdDataItemRefT1.SingleValue] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[StdDataItemRefT1.ValueRange] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
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
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )

    @dataclass(kw_only=True)
    class SingleValue(SingleValueT2):
        value: object = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ValueRange(ValueRangeT2):
        lower_value: object = field(
            metadata={
                "name": "lowerValue",
                "type": "Attribute",
                "required": True,
            }
        )
        upper_value: object = field(
            metadata={
                "name": "upperValue",
                "type": "Attribute",
                "required": True,
            }
        )
