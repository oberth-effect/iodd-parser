from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.single_value_t import SingleValueT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IntegerValueT(SingleValueT):
    value: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
