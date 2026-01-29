from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_2 import CollectionT2
from iodd_parser.generated.v1_1.event_desc_t_2 import EventDescT2
from iodd_parser.generated.v1_1.std_event_ref_t_2 import StdEventRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class EventCollectionT2(CollectionT2):
    class Meta:
        name = "EventCollectionT"

    std_event_ref: list[StdEventRefT2] = field(
        default_factory=list,
        metadata={
            "name": "StdEventRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    event: list[EventDescT2] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
