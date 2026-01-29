from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t_1 import AccessRightsT1
from iodd_parser.generated.v1_1.data_item_t_2 import DataItemT2
from iodd_parser.generated.v1_1.record_item_info_t_2 import RecordItemInfoT2
from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class AbstractVariableT2(DataItemT2):
    class Meta:
        name = "AbstractVariableT"

    record_item_info: list[RecordItemInfoT2] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    name: TextRefT1 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT1 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    access_rights: AccessRightsT1 = field(
        metadata={
            "name": "accessRights",
            "type": "Attribute",
            "required": True,
        }
    )
    dynamic: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )
