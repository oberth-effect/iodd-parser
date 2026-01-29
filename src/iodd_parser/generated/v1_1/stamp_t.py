from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class StampT:
    checker: StampT.Checker = field(
        metadata={
            "name": "Checker",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    crc: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Checker:
        name: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        version: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"V\d+(\.\d+){1,7}",
            }
        )
