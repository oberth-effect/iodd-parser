from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1
from iodd_parser.generated.v1_1.wire_color_t import WireColorT
from iodd_parser.generated.v1_1.wire_function_t import WireFunctionT
from iodd_parser.generated.v1_1.wire_t import WireT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class WireAnyT(WireT):
    name: TextRefT1 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    color: WireColorT = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    function: WireFunctionT = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
