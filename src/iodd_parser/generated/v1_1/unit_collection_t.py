from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UnitCollectionT(CollectionT1):
    unit: list[UnitCollectionT.Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Unit:
        code: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        abbr: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        text_id: str = field(
            metadata={
                "name": "textId",
                "type": "Attribute",
                "required": True,
                "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
            }
        )
