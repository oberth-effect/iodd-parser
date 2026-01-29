from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_2 import CollectionT2
from iodd_parser.generated.v1_1.datatype_t_2 import DatatypeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class DatatypeCollectionT2(CollectionT2):
    class Meta:
        name = "DatatypeCollectionT"

    datatype: list[DatatypeT2] = field(
        default_factory=list,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
