from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t_2 import TextRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ButtonT1:
    class Meta:
        name = "ButtonT"

    description: None | TextRefT2 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    action_started_message: None | TextRefT2 = field(
        default=None,
        metadata={
            "name": "ActionStartedMessage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    button_value: bool | int = field(
        metadata={
            "name": "buttonValue",
            "type": "Attribute",
            "required": True,
        }
    )
