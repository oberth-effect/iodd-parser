from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.menu_collection_t import MenuCollectionT
from iodd_parser.generated.v1_1.menu_set_t import MenuSetT
from iodd_parser.generated.v1_1.process_data_ref_collection_t import (
    ProcessDataRefCollectionT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UserInterfaceT:
    process_data_ref_collection: None | ProcessDataRefCollectionT = field(
        default=None,
        metadata={
            "name": "ProcessDataRefCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    menu_collection: MenuCollectionT = field(
        metadata={
            "name": "MenuCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    observer_role_menu_set: MenuSetT = field(
        metadata={
            "name": "ObserverRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    maintenance_role_menu_set: MenuSetT = field(
        metadata={
            "name": "MaintenanceRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    specialist_role_menu_set: MenuSetT = field(
        metadata={
            "name": "SpecialistRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
