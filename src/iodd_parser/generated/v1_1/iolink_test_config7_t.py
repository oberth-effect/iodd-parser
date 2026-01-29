from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iolink_test_event_t import IolinkTestEventT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkTestConfig7T:
    class Meta:
        name = "IOLinkTestConfig7T"

    event_trigger: list[IolinkTestEventT] = field(
        default_factory=list,
        metadata={
            "name": "EventTrigger",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
