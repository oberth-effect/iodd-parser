from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.device_variant_t import DeviceVariantT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DeviceVariantCollectionT(CollectionT1):
    device_variant: list[DeviceVariantT] = field(
        default_factory=list,
        metadata={
            "name": "DeviceVariant",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
