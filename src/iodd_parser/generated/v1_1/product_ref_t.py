from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProductRefT:
    product_id: str = field(
        metadata={
            "name": "productId",
            "type": "Attribute",
            "required": True,
        }
    )
