from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t_2 import TextRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ErrorTypeT2:
    class Meta:
        name = "ErrorTypeT"

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
    code: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    additional_code: int = field(
        metadata={
            "name": "additionalCode",
            "type": "Attribute",
            "required": True,
        }
    )
