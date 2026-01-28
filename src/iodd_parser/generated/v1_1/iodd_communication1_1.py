from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from iodd_parser.generated.v1_1.iodd_primitives1_1 import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class CommNetworkProfileT:
    pass


class IolinkCommNetworkProfileTCompatibleWith(Enum):
    V1_0 = "V1.0"


class IolinkPhysicalLayerTBitrate(Enum):
    COM1 = "COM1"
    COM2 = "COM2"
    COM3 = "COM3"


@dataclass(kw_only=True)
class IolinkTestConfigT:
    class Meta:
        name = "IOLinkTestConfigT"

    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    test_value: str = field(
        metadata={
            "name": "testValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"(0x[0-9A-Fa-f][0-9A-Fa-f],)*0x[0-9A-Fa-f][0-9A-Fa-f]",
        }
    )


@dataclass(kw_only=True)
class IolinkTestEventT:
    class Meta:
        name = "IOLinkTestEventT"

    appear_value: int = field(
        metadata={
            "name": "appearValue",
            "type": "Attribute",
            "required": True,
        }
    )
    disappear_value: int = field(
        metadata={
            "name": "disappearValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProductRefT:
    product_id: str = field(
        metadata={
            "name": "productId",
            "type": "Attribute",
            "required": True,
        }
    )


class Wire2Function1(Enum):
    NC = "NC"
    OTHER = "Other"


class Wire2Function2(Enum):
    NC = "NC"
    P24 = "P24"
    OTHER = "Other"


class Wire5Function(Enum):
    NC = "NC"
    N24 = "N24"


class WireColorT(Enum):
    """
    Codes according to IEC 60757-1983.
    """

    BK = "BK"
    BN = "BN"
    RD = "RD"
    OG = "OG"
    YE = "YE"
    GN = "GN"
    BU = "BU"
    VT = "VT"
    GY = "GY"
    WH = "WH"
    PK = "PK"
    GD = "GD"
    TQ = "TQ"
    SR = "SR"


class WireFunctionT(Enum):
    NC = "NC"
    L = "L+"
    L_1 = "L-"
    P24 = "P24"
    N24 = "N24"
    OTHER = "Other"
    C_Q = "C/Q"


@dataclass(kw_only=True)
class IolinkTestConfig7T:
    class Meta:
        name = "IOLinkTestConfig7T"

    event_trigger: list[IolinkTestEventT] = field(
        default_factory=list,
        metadata={
            "name": "EventTrigger",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class WireT:
    name: None | TextRefT = field(
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
    description: None | TextRefT = field(
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


@dataclass(kw_only=True)
class IolinkTestT:
    class Meta:
        name = "IOLinkTestT"

    config1: None | IolinkTestConfigT = field(
        default=None,
        metadata={
            "name": "Config1",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    config2: None | IolinkTestConfigT = field(
        default=None,
        metadata={
            "name": "Config2",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    config3: None | IolinkTestConfigT = field(
        default=None,
        metadata={
            "name": "Config3",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    config7: None | IolinkTestConfig7T = field(
        default=None,
        metadata={
            "name": "Config7",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class Wire1T(WireT):
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    color: WireColorT = field(
        init=False,
        default=WireColorT.BN,
        metadata={
            "type": "Attribute",
        },
    )
    function: WireFunctionT = field(
        init=False,
        default=WireFunctionT.L,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Wire3T(WireT):
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    color: WireColorT = field(
        init=False,
        default=WireColorT.BU,
        metadata={
            "type": "Attribute",
        },
    )
    function: WireFunctionT = field(
        init=False,
        default=WireFunctionT.L_1,
        metadata={
            "type": "Attribute",
        },
    )


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


@dataclass(kw_only=True)
class WireAnyT(WireT):
    name: TextRefT = field(
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


@dataclass(kw_only=True)
class CableConnectionT(ConnectionT):
    pass


@dataclass(kw_only=True)
class IolinkPhysicalLayerT:
    class Meta:
        name = "IOLinkPhysicalLayerT"

    connection: list[ConnectionT] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
    bitrate: IolinkPhysicalLayerTBitrate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    min_cycle_time: int = field(
        metadata={
            "name": "minCycleTime",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 132800,
        }
    )
    sio_supported: bool = field(
        metadata={
            "name": "sioSupported",
            "type": "Attribute",
            "required": True,
        }
    )
    m_sequence_capability: int = field(
        metadata={
            "name": "mSequenceCapability",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class M124ConnectionT(ConnectionT):
    class Meta:
        name = "M12-4ConnectionT"

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
    wire2: M124ConnectionT.Wire2 = field(
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


@dataclass(kw_only=True)
class M125ConnectionT(ConnectionT):
    class Meta:
        name = "M12-5ConnectionT"

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
    wire2: M125ConnectionT.Wire2 = field(
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
    wire5: M125ConnectionT.Wire5 = field(
        metadata={
            "name": "Wire5",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Wire2(WireT):
        color: WireColorT = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        function: Wire2Function2 = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Wire5(WireT):
        color: WireColorT = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        function: Wire5Function = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class M5ConnectionT(ConnectionT):
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
    wire2: M5ConnectionT.Wire2 = field(
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


@dataclass(kw_only=True)
class OtherConnectionT(ConnectionT):
    description: TextRefT = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IolinkTransportLayersT:
    class Meta:
        name = "IOLinkTransportLayersT"

    physical_layer: IolinkPhysicalLayerT = field(
        metadata={
            "name": "PhysicalLayer",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IolinkCommNetworkProfileT(CommNetworkProfileT):
    class Meta:
        name = "IOLinkCommNetworkProfileT"

    transport_layers: IolinkTransportLayersT = field(
        metadata={
            "name": "TransportLayers",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    test: IolinkTestT = field(
        metadata={
            "name": "Test",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    iolink_revision: str = field(
        init=False,
        default="V1.1",
        metadata={
            "name": "iolinkRevision",
            "type": "Attribute",
            "required": True,
            "pattern": r"V\d+(\.\d+){1,7}",
        },
    )
    compatible_with: None | IolinkCommNetworkProfileTCompatibleWith = field(
        default=None,
        metadata={
            "name": "compatibleWith",
            "type": "Attribute",
        },
    )
