from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t_2 import AccessRightsT2
from iodd_parser.generated.v1_1.button_t_1 import ButtonT1
from iodd_parser.generated.v1_1.process_data_info_t_1 import ProcessDataInfoT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class UidataItemRefT1(ProcessDataInfoT1):
    class Meta:
        name = "UIDataItemRefT"

    button: None | ButtonT1 = field(
        default=None,
        metadata={
            "name": "Button",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable_id: str = field(
        metadata={
            "name": "variableId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    access_right_restriction: None | AccessRightsT2 = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )
