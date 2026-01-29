from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ButtonT2:
    class Meta:
        name = "ButtonT"

    description: None | TextRefT1 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    action_started_message: None | TextRefT1 = field(
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
