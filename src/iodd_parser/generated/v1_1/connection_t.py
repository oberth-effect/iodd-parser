from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.product_ref_t import ProductRefT
from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1
from iodd_parser.generated.v1_1.wire_t import WireT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ConnectionT:
    product_ref: list[ProductRefT] = field(
        default_factory=list,
        metadata={
            "name": "ProductRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
    description: None | TextRefT1 = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire1: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire1",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire2: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire2",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire3: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire3",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire4: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire4",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire5: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire5",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire6: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire6",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire7: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire7",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire8: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire8",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    wire9: None | WireT = field(
        default=None,
        metadata={
            "name": "Wire9",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    connection_symbol: None | str = field(
        default=None,
        metadata={
            "name": "connectionSymbol",
            "type": "Attribute",
            "pattern": r"([\p{L}\d_#]+-)+con-pic\.png",
        },
    )
