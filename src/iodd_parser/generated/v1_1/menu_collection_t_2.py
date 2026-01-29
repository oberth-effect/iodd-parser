from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.menu_t_2 import MenuT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class MenuCollectionT2(CollectionT1):
    class Meta:
        name = "MenuCollectionT"

    menu: list[MenuT2] = field(
        default_factory=list,
        metadata={
            "name": "Menu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
