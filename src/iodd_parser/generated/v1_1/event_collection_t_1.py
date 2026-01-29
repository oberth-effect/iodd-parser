from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.event_desc_t_1 import EventDescT1
from iodd_parser.generated.v1_1.std_event_ref_t_1 import StdEventRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class EventCollectionT1(CollectionT1):
    class Meta:
        name = "EventCollectionT"

    std_event_ref: list[StdEventRefT1] = field(
        default_factory=list,
        metadata={
            "name": "StdEventRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    event: list[EventDescT1] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
