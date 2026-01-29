from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.menu_collection_t_2 import MenuCollectionT2
from iodd_parser.generated.v1_1.menu_set_t_2 import MenuSetT2
from iodd_parser.generated.v1_1.process_data_ref_collection_t_2 import (
    ProcessDataRefCollectionT2,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UserInterfaceT2:
    class Meta:
        name = "UserInterfaceT"

    process_data_ref_collection: None | ProcessDataRefCollectionT2 = field(
        default=None,
        metadata={
            "name": "ProcessDataRefCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    menu_collection: MenuCollectionT2 = field(
        metadata={
            "name": "MenuCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    observer_role_menu_set: MenuSetT2 = field(
        metadata={
            "name": "ObserverRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    maintenance_role_menu_set: MenuSetT2 = field(
        metadata={
            "name": "MaintenanceRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    specialist_role_menu_set: MenuSetT2 = field(
        metadata={
            "name": "SpecialistRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
