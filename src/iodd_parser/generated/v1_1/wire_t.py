from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1
from iodd_parser.generated.v1_1.wire_color_t import WireColorT
from iodd_parser.generated.v1_1.wire_function_t import WireFunctionT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class WireT:
    name: None | TextRefT1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    color: None | WireColorT = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    function: None | WireFunctionT = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
