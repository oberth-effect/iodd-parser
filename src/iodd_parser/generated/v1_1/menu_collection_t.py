from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t import CollectionT
from iodd_parser.generated.v1_1.menu_t import MenuT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class MenuCollectionT(CollectionT):
    menu: list[MenuT] = field(
        default_factory=list,
        metadata={
            "name": "Menu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
