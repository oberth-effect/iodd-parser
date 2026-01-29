from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.comm_network_profile_t import (
    CommNetworkProfileT,
)
from iodd_parser.generated.v1_1.document_info_t import DocumentInfoT
from iodd_parser.generated.v1_1.external_text_collection_t import (
    ExternalTextCollectionT,
)
from iodd_parser.generated.v1_1.profile_body_t import ProfileBodyT
from iodd_parser.generated.v1_1.profile_header_t import ProfileHeaderT
from iodd_parser.generated.v1_1.stamp_t import StampT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class Iodevice:
    """
    :ivar document_info:
    :ivar profile_header:
    :ivar profile_body:
    :ivar comm_network_profile:
    :ivar external_text_collection:
    :ivar stamp: Filled out by the IODD Checker.
    """

    class Meta:
        name = "IODevice"
        namespace = "http://www.io-link.com/IODD/2010/10"

    document_info: DocumentInfoT = field(
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "required": True,
        }
    )
    profile_header: ProfileHeaderT = field(
        metadata={
            "name": "ProfileHeader",
            "type": "Element",
            "required": True,
        }
    )
    profile_body: ProfileBodyT = field(
        metadata={
            "name": "ProfileBody",
            "type": "Element",
            "required": True,
        }
    )
    comm_network_profile: CommNetworkProfileT = field(
        metadata={
            "name": "CommNetworkProfile",
            "type": "Element",
            "required": True,
        }
    )
    external_text_collection: ExternalTextCollectionT = field(
        metadata={
            "name": "ExternalTextCollection",
            "type": "Element",
            "required": True,
        }
    )
    stamp: StampT = field(
        metadata={
            "name": "Stamp",
            "type": "Element",
            "required": True,
        }
    )
