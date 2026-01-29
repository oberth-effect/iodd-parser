from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t import TextRefT
from iodd_parser.generated.v1_1.uimenu_ref_t import UimenuRefT
from iodd_parser.generated.v1_1.uirecord_item_ref_t import UirecordItemRefT
from iodd_parser.generated.v1_1.uivariable_ref_t import UivariableRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
