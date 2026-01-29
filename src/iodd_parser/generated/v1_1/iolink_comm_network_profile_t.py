from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.comm_network_profile_t import (
    CommNetworkProfileT,
)
from iodd_parser.generated.v1_1.iolink_comm_network_profile_t_compatible_with import (
    IolinkCommNetworkProfileTCompatibleWith,
)
from iodd_parser.generated.v1_1.iolink_test_t import IolinkTestT
from iodd_parser.generated.v1_1.iolink_transport_layers_t import (
    IolinkTransportLayersT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
