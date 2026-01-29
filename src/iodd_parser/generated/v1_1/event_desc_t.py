from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.event_desc_t_type import EventDescTType
from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class EventDescT:
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
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
    type_value: EventDescTType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
