from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.boolean_value_t_2 import BooleanValueT2
from iodd_parser.generated.v1_1.simple_datatype_t_2 import SimpleDatatypeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class BooleanT2(SimpleDatatypeT2):
    class Meta:
        name = "BooleanT"

    single_value: list[BooleanValueT2] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
