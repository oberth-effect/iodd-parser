from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkTestEventT:
    class Meta:
        name = "IOLinkTestEventT"

    appear_value: int = field(
        metadata={
            "name": "appearValue",
            "type": "Attribute",
            "required": True,
        }
    )
    disappear_value: int = field(
        metadata={
            "name": "disappearValue",
            "type": "Attribute",
            "required": True,
        }
    )
