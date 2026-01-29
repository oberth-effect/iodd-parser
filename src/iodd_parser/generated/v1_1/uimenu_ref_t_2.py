from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.condition_t_1 import ConditionT1
from iodd_parser.generated.v1_1.uimenu_ref_simple_t_2 import UimenuRefSimpleT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UimenuRefT2(UimenuRefSimpleT2):
    class Meta:
        name = "UIMenuRefT"

    condition: None | ConditionT1 = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
