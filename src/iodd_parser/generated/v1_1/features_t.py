from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.supported_access_locks_t import (
    SupportedAccessLocksT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class FeaturesT:
    supported_access_locks: None | SupportedAccessLocksT = field(
        default=None,
        metadata={
            "name": "SupportedAccessLocks",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    block_parameter: bool = field(
        metadata={
            "name": "blockParameter",
            "type": "Attribute",
            "required": True,
        }
    )
    data_storage: bool = field(
        metadata={
            "name": "dataStorage",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_characteristic: list[int] = field(
        default_factory=list,
        metadata={
            "name": "profileCharacteristic",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
            "tokens": True,
        },
    )
