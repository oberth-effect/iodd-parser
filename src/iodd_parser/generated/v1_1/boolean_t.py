from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.boolean_value_t import BooleanValueT
from iodd_parser.generated.v1_1.simple_datatype_t import SimpleDatatypeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class BooleanT(SimpleDatatypeT):
    single_value: list[BooleanValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "max_occurs": 2,
        },
    )
