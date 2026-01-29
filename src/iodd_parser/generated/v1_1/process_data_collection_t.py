from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t import CollectionT
from iodd_parser.generated.v1_1.process_data_t import ProcessDataT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataCollectionT(CollectionT):
    process_data: list[ProcessDataT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessData",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
