from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class SupportedAccessLocksT:
    parameter: bool = field(
        metadata={
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
    local_parameterization: bool = field(
        metadata={
            "name": "localParameterization",
            "type": "Attribute",
            "required": True,
        }
    )
    local_user_interface: bool = field(
        metadata={
            "name": "localUserInterface",
            "type": "Attribute",
            "required": True,
        }
    )
