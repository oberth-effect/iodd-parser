from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.menu_collection_t_1 import MenuCollectionT1
from iodd_parser.generated.v1_1.menu_set_t_1 import MenuSetT1
from iodd_parser.generated.v1_1.process_data_ref_collection_t_1 import (
    ProcessDataRefCollectionT1,
)

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class UserInterfaceT1:
    class Meta:
        name = "UserInterfaceT"

    process_data_ref_collection: None | ProcessDataRefCollectionT1 = field(
        default=None,
        metadata={
            "name": "ProcessDataRefCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    menu_collection: MenuCollectionT1 = field(
        metadata={
            "name": "MenuCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    observer_role_menu_set: MenuSetT1 = field(
        metadata={
            "name": "ObserverRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    maintenance_role_menu_set: MenuSetT1 = field(
        metadata={
            "name": "MaintenanceRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    specialist_role_menu_set: MenuSetT1 = field(
        metadata={
            "name": "SpecialistRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
