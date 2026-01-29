from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t import CollectionT
from iodd_parser.generated.v1_1.event_desc_t import EventDescT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IoddstandardEventCollectionT(CollectionT):
    class Meta:
        name = "IODDStandardEventCollectionT"

    event: list[EventDescT] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
