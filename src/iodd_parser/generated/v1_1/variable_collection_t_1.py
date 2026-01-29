from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_2 import CollectionT2
from iodd_parser.generated.v1_1.std_variable_ref_t_1 import StdVariableRefT1
from iodd_parser.generated.v1_1.variable_t_1 import VariableT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class VariableCollectionT1(CollectionT2):
    class Meta:
        name = "VariableCollectionT"

    std_variable_ref: list[StdVariableRefT1] = field(
        default_factory=list,
        metadata={
            "name": "StdVariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable: list[VariableCollectionT1.Variable] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
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

    @dataclass(kw_only=True)
    class Variable(VariableT1):
        default_value: None | object = field(
            default=None,
            metadata={
                "name": "defaultValue",
                "type": "Attribute",
            },
        )
