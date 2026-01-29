from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.single_value_t_2 import SingleValueT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class TbdValueT(SingleValueT2):
    value: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
