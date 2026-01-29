from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.condition_t_2 import ConditionT2
from iodd_parser.generated.v1_1.uimenu_ref_simple_t_1 import UimenuRefSimpleT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class UimenuRefT1(UimenuRefSimpleT1):
    class Meta:
        name = "UIMenuRefT"

    condition: None | ConditionT2 = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
