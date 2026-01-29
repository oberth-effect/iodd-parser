from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.comm_network_profile_t import (
    CommNetworkProfileT,
)
from iodd_parser.generated.v1_1.iolink_test_t import IolinkTestT
from iodd_parser.generated.v1_1.iolink_wireless_transport_layers_t import (
    IolinkWirelessTransportLayersT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkWirelessCommNetworkProfileT(CommNetworkProfileT):
    class Meta:
        name = "IOLinkWirelessCommNetworkProfileT"

    transport_layers: IolinkWirelessTransportLayersT = field(
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
    iolink_wireless_revision: str = field(
        metadata={
            "name": "iolinkWirelessRevision",
            "type": "Attribute",
            "required": True,
            "pattern": r"V\d+(\.\d+){1,7}",
        }
    )
