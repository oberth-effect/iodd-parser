from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.condition_t import ConditionT
from iodd_parser.generated.v1_1.uimenu_ref_simple_t import UimenuRefSimpleT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
