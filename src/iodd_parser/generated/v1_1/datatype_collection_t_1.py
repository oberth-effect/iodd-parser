from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.datatype_t_1 import DatatypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DatatypeCollectionT1(CollectionT1):
    class Meta:
        name = "DatatypeCollectionT"

    datatype: list[DatatypeT1] = field(
        default_factory=list,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
