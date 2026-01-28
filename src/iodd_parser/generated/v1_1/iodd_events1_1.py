from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from iodd_parser.generated.v1_1.iodd_primitives1_1 import (
    CollectionT,
    TextRefT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


class EventDescTType(Enum):
    NOTIFICATION = "Notification"
    WARNING = "Warning"
    ERROR = "Error"


@dataclass(kw_only=True)
class StdErrorTypeRefT:
    code: int = field(
        init=False,
        default=128,
        metadata={
            "type": "Attribute",
        },
    )
    additional_code: int = field(
        metadata={
            "name": "additionalCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StdEventRefT:
    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ErrorTypeT:
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    additional_code: int = field(
        metadata={
            "name": "additionalCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EventDescT:
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: EventDescTType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ErrorType129T(ErrorTypeT):
    code: int = field(
        init=False,
        default=129,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EventCollectionT(CollectionT):
    std_event_ref: list[StdEventRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdEventRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    event: list[EventDescT] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class ErrorTypeCollectionT(CollectionT):
    std_error_type_ref: list[StdErrorTypeRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdErrorTypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    error_type: list[ErrorType129T] = field(
        default_factory=list,
        metadata={
            "name": "ErrorType",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
