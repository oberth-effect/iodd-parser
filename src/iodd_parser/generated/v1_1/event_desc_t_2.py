from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.event_desc_t_type_2 import EventDescTType2
from iodd_parser.generated.v1_1.text_ref_t_2 import TextRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class EventDescT2:
    class Meta:
        name = "EventDescT"

    name: TextRefT2 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    description: None | TextRefT2 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: EventDescTType2 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
