from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.abstract_variable_t_2 import AbstractVariableT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class VariableT2(AbstractVariableT2):
    class Meta:
        name = "VariableT"

    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
