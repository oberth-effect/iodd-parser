from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ButtonT:
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    action_started_message: None | TextRefT = field(
        default=None,
        metadata={
            "name": "ActionStartedMessage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    button_value: bool | int = field(
        metadata={
            "name": "buttonValue",
            "type": "Attribute",
            "required": True,
        }
    )
