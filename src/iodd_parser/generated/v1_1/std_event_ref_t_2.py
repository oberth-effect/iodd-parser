from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class StdEventRefT2:
    class Meta:
        name = "StdEventRefT"

    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
