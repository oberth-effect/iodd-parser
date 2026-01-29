from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.single_value_t_1 import SingleValueT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class BooleanValueT1(SingleValueT1):
    class Meta:
        name = "BooleanValueT"

    value: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
