from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1
from iodd_parser.generated.v1_1.uimenu_ref_t_2 import UimenuRefT2
from iodd_parser.generated.v1_1.uirecord_item_ref_t_2 import UirecordItemRefT2
from iodd_parser.generated.v1_1.uivariable_ref_t_2 import UivariableRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class MenuT2:
    class Meta:
        name = "MenuT"

    name: None | TextRefT1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable_ref: list[UivariableRefT2] = field(
        default_factory=list,
        metadata={
            "name": "VariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    record_item_ref: list[UirecordItemRefT2] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    menu_ref: list[UimenuRefT2] = field(
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
