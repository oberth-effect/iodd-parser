from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.connection_t import ConnectionT
from iodd_parser.generated.v1_1.iolink_wireless_physical_layer_t_default_slot_type import (
    IolinkWirelessPhysicalLayerTDefaultSlotType,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkWirelessPhysicalLayerT:
    class Meta:
        name = "IOLinkWirelessPhysicalLayerT"

    connection: list[ConnectionT] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
    wmin_cycle_time_out: object = field(
        metadata={
            "name": "WMinCycleTimeOut",
            "type": "Attribute",
            "required": True,
        }
    )
    wmin_cycle_time_in: object = field(
        metadata={
            "name": "WMinCycleTimeIn",
            "type": "Attribute",
            "required": True,
        }
    )
    max_tx_power: int = field(
        metadata={
            "name": "maxTxPower",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -20,
            "max_inclusive": 10,
        }
    )
    default_slot_type: IolinkWirelessPhysicalLayerTDefaultSlotType = field(
        metadata={
            "name": "defaultSlotType",
            "type": "Attribute",
            "required": True,
        }
    )
    is_abridge: bool = field(
        default=False,
        metadata={
            "name": "isABridge",
            "type": "Attribute",
        },
    )
    is_low_power_device: bool = field(
        default=False,
        metadata={
            "name": "isLowPowerDevice",
            "type": "Attribute",
        },
    )
