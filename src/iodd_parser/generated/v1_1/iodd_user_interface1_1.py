from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from iodd_parser.generated.v1_1.iodd_primitives1_1 import (
    AccessRightsT,
    CollectionT,
    ConditionT,
    TextRefT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataInfoT:
    gradient: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    offset: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit_code: None | int = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    display_format: None | str = field(
        default=None,
        metadata={
            "name": "displayFormat",
            "type": "Attribute",
            "pattern": r"Bin|Hex|Dec(\.\d)?",
        },
    )


@dataclass(kw_only=True)
class UimenuRefSimpleT:
    class Meta:
        name = "UIMenuRefSimpleT"

    menu_id: str = field(
        metadata={
            "name": "menuId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )


@dataclass(kw_only=True)
class ButtonT:
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    action_started_message: None | TextRefT = field(
        default=None,
        metadata={
            "name": "ActionStartedMessage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    button_value: bool | int = field(
        metadata={
            "name": "buttonValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MenuSetT:
    identification_menu: UimenuRefSimpleT = field(
        metadata={
            "name": "IdentificationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    parameter_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "ParameterMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    observation_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "ObservationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    diagnosis_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "DiagnosisMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class ProcessDataRecordItemInfoT(ProcessDataInfoT):
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass(kw_only=True)
class UimenuRefT(UimenuRefSimpleT):
    class Meta:
        name = "UIMenuRefT"

    condition: None | ConditionT = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class ProcessDataRefT:
    process_data_info: None | ProcessDataInfoT = field(
        default=None,
        metadata={
            "name": "ProcessDataInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_record_item_info: list[ProcessDataRecordItemInfoT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_id: str = field(
        metadata={
            "name": "processDataId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )


@dataclass(kw_only=True)
class UidataItemRefT(ProcessDataInfoT):
    class Meta:
        name = "UIDataItemRefT"

    button: None | ButtonT = field(
        default=None,
        metadata={
            "name": "Button",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable_id: str = field(
        metadata={
            "name": "variableId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    access_right_restriction: None | AccessRightsT = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProcessDataRefCollectionT:
    process_data_ref: list[ProcessDataRefT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class UirecordItemRefT(UidataItemRefT):
    class Meta:
        name = "UIRecordItemRefT"

    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass(kw_only=True)
class UivariableRefT(UidataItemRefT):
    class Meta:
        name = "UIVariableRefT"


@dataclass(kw_only=True)
class MenuT:
    name: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable_ref: list[UivariableRefT] = field(
        default_factory=list,
        metadata={
            "name": "VariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    record_item_ref: list[UirecordItemRefT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    menu_ref: list[UimenuRefT] = field(
        default_factory=list,
        metadata={
            "name": "MenuRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )


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
