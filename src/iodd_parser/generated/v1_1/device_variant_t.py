from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DeviceVariantT:
    """
    :ivar name:
    :ivar description:
    :ivar product_id: This must be the same product ID as returned by
        the corresponding IO-Link index. This ensures unique
        identification of the device during scanning.
    :ivar device_symbol: The symbol shall be available as PNG, 160x160
        pixels. The filename must not have a path prefix and shall
        follow the naming rules.
    :ivar device_icon: The icon shall be available as PNG, 48x48 pixels.
        The filename must not have a path prefix and shall follow the
        naming rules.
    """

    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: TextRefT = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    product_id: str = field(
        metadata={
            "name": "productId",
            "type": "Attribute",
            "required": True,
        }
    )
    device_symbol: None | str = field(
        default=None,
        metadata={
            "name": "deviceSymbol",
            "type": "Attribute",
            "pattern": r"([\p{L}\d_#]+-)+pic\.png",
        },
    )
    device_icon: None | str = field(
        default=None,
        metadata={
            "name": "deviceIcon",
            "type": "Attribute",
            "pattern": r"([\p{L}\d_#]+-)+icon\.png",
        },
    )
