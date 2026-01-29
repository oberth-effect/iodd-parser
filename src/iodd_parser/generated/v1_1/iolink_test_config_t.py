from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkTestConfigT:
    class Meta:
        name = "IOLinkTestConfigT"

    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    test_value: str = field(
        metadata={
            "name": "testValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"(0x[0-9A-Fa-f][0-9A-Fa-f],)*0x[0-9A-Fa-f][0-9A-Fa-f]",
        }
    )
