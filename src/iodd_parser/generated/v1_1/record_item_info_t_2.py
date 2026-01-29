from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class RecordItemInfoT2:
    class Meta:
        name = "RecordItemInfoT"

    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )
