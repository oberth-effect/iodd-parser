from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.device_function_t import DeviceFunctionT
from iodd_parser.generated.v1_1.device_identity_t import DeviceIdentityT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProfileBodyT:
    device_identity: DeviceIdentityT = field(
        metadata={
            "name": "DeviceIdentity",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    device_function: DeviceFunctionT = field(
        metadata={
            "name": "DeviceFunction",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
