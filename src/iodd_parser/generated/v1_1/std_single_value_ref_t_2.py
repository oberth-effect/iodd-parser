from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StdSingleValueRefT2:
    class Meta:
        name = "StdSingleValueRefT"

    value: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
