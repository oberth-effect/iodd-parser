from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.variable_t_2 import VariableT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IoddstandardVariableT(VariableT2):
    class Meta:
        name = "IODDStandardVariableT"

    mandatory: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
