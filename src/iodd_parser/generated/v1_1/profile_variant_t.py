from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ProfileVariantT:
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
    profile_option: None | str = field(
        default=None,
        metadata={
            "name": "profileOption",
            "type": "Attribute",
            "pattern": r"(\d+( XOR \d+)+|\d+\.\.\d+|\d+)(, *(\d+( XOR \d+)+|\d+\.\.\d+|\d+))*",
        },
    )
    info: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
