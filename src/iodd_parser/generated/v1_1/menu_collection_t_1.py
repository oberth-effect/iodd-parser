from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_2 import CollectionT2
from iodd_parser.generated.v1_1.menu_t_1 import MenuT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class MenuCollectionT1(CollectionT2):
    class Meta:
        name = "MenuCollectionT"

    menu: list[MenuT1] = field(
        default_factory=list,
        metadata={
            "name": "Menu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
