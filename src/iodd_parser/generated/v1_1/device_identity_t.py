from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.device_variant_collection_t import (
    DeviceVariantCollectionT,
)
from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DeviceIdentityT:
    """
    :ivar vendor_text:
    :ivar vendor_url:
    :ivar vendor_logo: This logo shall be available as PNG, 160x90
        pixels. The filename must not have a path prefix and shall
        follow the naming rules.
    :ivar device_name:
    :ivar device_family:
    :ivar device_variant_collection:
    :ivar vendor_id:
    :ivar vendor_name:
    :ivar device_id:
    :ivar additional_device_ids:
    """

    vendor_text: TextRefT1 = field(
        metadata={
            "name": "VendorText",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    vendor_url: TextRefT1 = field(
        metadata={
            "name": "VendorUrl",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    vendor_logo: None | DeviceIdentityT.VendorLogo = field(
        default=None,
        metadata={
            "name": "VendorLogo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    device_name: TextRefT1 = field(
        metadata={
            "name": "DeviceName",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    device_family: TextRefT1 = field(
        metadata={
            "name": "DeviceFamily",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    device_variant_collection: DeviceVariantCollectionT = field(
        metadata={
            "name": "DeviceVariantCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    vendor_id: int = field(
        metadata={
            "name": "vendorId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    vendor_name: str = field(
        metadata={
            "name": "vendorName",
            "type": "Attribute",
            "required": True,
        }
    )
    device_id: int = field(
        metadata={
            "name": "deviceId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 16777215,
        }
    )
    additional_device_ids: list[int] = field(
        default_factory=list,
        metadata={
            "name": "additionalDeviceIds",
            "type": "Attribute",
            "min_inclusive": 1,
            "min_length": 1,
            "max_inclusive": 16777215,
            "max_length": 255,
            "tokens": True,
        },
    )

    @dataclass(kw_only=True)
    class VendorLogo:
        name: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"([\p{L}\d_#]+-)+logo\.png",
            }
        )
