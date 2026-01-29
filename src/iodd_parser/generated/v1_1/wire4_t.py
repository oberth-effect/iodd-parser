from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from iodd_parser.generated.v1_1.wire_color_t import WireColorT
from iodd_parser.generated.v1_1.wire_function_t import WireFunctionT
from iodd_parser.generated.v1_1.wire_t import WireT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class Wire4T(WireT):
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    color: WireColorT = field(
        init=False,
        default=WireColorT.BK,
        metadata={
            "type": "Attribute",
        },
    )
    function: WireFunctionT = field(
        default=WireFunctionT.C_Q,
        metadata={
            "type": "Attribute",
        },
    )
