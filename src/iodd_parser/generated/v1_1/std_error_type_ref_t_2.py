from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class StdErrorTypeRefT2:
    class Meta:
        name = "StdErrorTypeRefT"

    code: int = field(
        init=False,
        default=128,
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
