from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataInfoT2:
    class Meta:
        name = "ProcessDataInfoT"

    gradient: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    offset: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit_code: None | int = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        },
    )
    display_format: None | str = field(
        default=None,
        metadata={
            "name": "displayFormat",
            "type": "Attribute",
            "pattern": r"Bin|Hex|Dec(\.\d)?",
        },
    )
