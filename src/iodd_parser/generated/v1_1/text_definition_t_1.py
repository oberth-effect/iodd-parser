from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class TextDefinitionT1:
    class Meta:
        name = "TextDefinitionT"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    value: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
