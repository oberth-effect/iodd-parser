from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iolink_physical_layer_t import (
    IolinkPhysicalLayerT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
