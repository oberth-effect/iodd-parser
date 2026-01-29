from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.event_desc_t_type_1 import EventDescTType1
from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class EventDescT1:
    class Meta:
        name = "EventDescT"

    name: TextRefT1 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT1 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: EventDescTType1 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
