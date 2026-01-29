from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iolink_wireless_physical_layer_t import (
    IolinkWirelessPhysicalLayerT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkWirelessTransportLayersT:
    class Meta:
        name = "IOLinkWirelessTransportLayersT"

    physical_layer: IolinkWirelessPhysicalLayerT = field(
        metadata={
            "name": "PhysicalLayer",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
