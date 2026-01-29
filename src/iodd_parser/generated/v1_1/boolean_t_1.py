from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.boolean_value_t_1 import BooleanValueT1
from iodd_parser.generated.v1_1.simple_datatype_t_1 import SimpleDatatypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class BooleanT1(SimpleDatatypeT1):
    class Meta:
        name = "BooleanT"

    single_value: list[BooleanValueT1] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "max_occurs": 2,
        },
    )
