from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.abstract_variable_t_2 import AbstractVariableT2
from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.std_variable_ref_t_2 import StdVariableRefT2
from iodd_parser.generated.v1_1.variable_t_2 import VariableT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class VariableCollectionT2(CollectionT1):
    class Meta:
        name = "VariableCollectionT"

    std_variable_ref: list[StdVariableRefT2] = field(
        default_factory=list,
        metadata={
            "name": "StdVariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 2,
        },
    )
    direct_parameter_overlay: None | AbstractVariableT2 = field(
        default=None,
        metadata={
            "name": "DirectParameterOverlay",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable: list[VariableCollectionT2.Variable] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )

    @dataclass(kw_only=True)
    class Variable(VariableT2):
        default_value: None | object = field(
            default=None,
            metadata={
                "name": "defaultValue",
                "type": "Attribute",
            },
        )
