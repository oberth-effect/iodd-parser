from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t import AccessRightsT
from iodd_parser.generated.v1_1.button_t import ButtonT
from iodd_parser.generated.v1_1.process_data_info_t import ProcessDataInfoT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
