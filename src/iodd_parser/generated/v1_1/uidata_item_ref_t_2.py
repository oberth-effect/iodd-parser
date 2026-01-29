from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t_1 import AccessRightsT1
from iodd_parser.generated.v1_1.button_t_2 import ButtonT2
from iodd_parser.generated.v1_1.process_data_info_t_2 import ProcessDataInfoT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UidataItemRefT2(ProcessDataInfoT2):
    class Meta:
        name = "UIDataItemRefT"

    button: None | ButtonT2 = field(
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
    access_right_restriction: None | AccessRightsT1 = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )
