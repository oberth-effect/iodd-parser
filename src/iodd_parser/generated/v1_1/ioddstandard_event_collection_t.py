from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.event_desc_t_1 import EventDescT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IoddstandardEventCollectionT(CollectionT1):
    class Meta:
        name = "IODDStandardEventCollectionT"

    event: list[EventDescT1] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
