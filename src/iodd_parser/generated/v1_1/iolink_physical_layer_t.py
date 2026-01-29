from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.connection_t import ConnectionT
from iodd_parser.generated.v1_1.iolink_physical_layer_t_bitrate import (
    IolinkPhysicalLayerTBitrate,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
