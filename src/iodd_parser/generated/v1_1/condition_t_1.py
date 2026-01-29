from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ConditionT1:
    class Meta:
        name = "ConditionT"

    variable_id: str = field(
        metadata={
            "name": "variableId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    subindex: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    value: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
