from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t import AccessRightsT
from iodd_parser.generated.v1_1.data_item_t import DataItemT
from iodd_parser.generated.v1_1.record_item_info_t import RecordItemInfoT
from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class AbstractVariableT(DataItemT):
    record_item_info: list[RecordItemInfoT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    access_rights: AccessRightsT = field(
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
