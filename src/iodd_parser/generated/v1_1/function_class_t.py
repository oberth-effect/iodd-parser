from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class FunctionClassT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    profile_id: int = field(
        metadata={
            "name": "profileId",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    profile_context: str = field(
        metadata={
            "name": "profileContext",
            "type": "Attribute",
            "required": True,
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        }
    )
