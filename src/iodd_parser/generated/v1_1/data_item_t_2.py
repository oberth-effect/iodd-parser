from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_ref_t_1 import DatatypeRefT1
from iodd_parser.generated.v1_1.datatype_t_1 import DatatypeT1
from iodd_parser.generated.v1_1.object_t_1 import ObjectT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DataItemT2(ObjectT1):
    class Meta:
        name = "DataItemT"

    datatype: None | DatatypeT1 = field(
        default=None,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    datatype_ref: None | DatatypeRefT1 = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
