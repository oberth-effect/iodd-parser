from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.abstract_variable_t import AbstractVariableT
from iodd_parser.generated.v1_1.collection_t import CollectionT
from iodd_parser.generated.v1_1.std_variable_ref_t import StdVariableRefT
from iodd_parser.generated.v1_1.variable_t import VariableT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class VariableCollectionT(CollectionT):
    std_variable_ref: list[StdVariableRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdVariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 2,
        },
    )
    direct_parameter_overlay: None | AbstractVariableT = field(
        default=None,
        metadata={
            "name": "DirectParameterOverlay",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable: list[VariableCollectionT.Variable] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )

    @dataclass(kw_only=True)
    class Variable(VariableT):
        default_value: None | object = field(
            default=None,
            metadata={
                "name": "defaultValue",
                "type": "Attribute",
            },
        )
