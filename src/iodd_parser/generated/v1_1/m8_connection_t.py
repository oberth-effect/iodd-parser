from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from iodd_parser.generated.v1_1.connection_t import ConnectionT
from iodd_parser.generated.v1_1.wire1_t import Wire1T
from iodd_parser.generated.v1_1.wire2_function_1 import Wire2Function1
from iodd_parser.generated.v1_1.wire3_t import Wire3T
from iodd_parser.generated.v1_1.wire4_t import Wire4T
from iodd_parser.generated.v1_1.wire_color_t import WireColorT
from iodd_parser.generated.v1_1.wire_t import WireT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class M8ConnectionT(ConnectionT):
    wire5: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    wire6: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    wire7: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    wire8: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    wire9: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    wire1: Wire1T = field(
        metadata={
            "name": "Wire1",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    wire2: M8ConnectionT.Wire2 = field(
        metadata={
            "name": "Wire2",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    wire3: Wire3T = field(
        metadata={
            "name": "Wire3",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    wire4: Wire4T = field(
        metadata={
            "name": "Wire4",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Wire2(WireT):
        color: WireColorT = field(
            init=False,
            default=WireColorT.WH,
            metadata={
                "type": "Attribute",
            },
        )
        function: Wire2Function1 = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
