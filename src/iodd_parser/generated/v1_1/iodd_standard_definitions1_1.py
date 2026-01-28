from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iodd_datatypes1_1 import DatatypeCollectionT
from iodd_parser.generated.v1_1.iodd_events1_1 import (
    ErrorTypeT,
    EventDescT,
)
from iodd_parser.generated.v1_1.iodd_primitives1_1 import (
    CollectionT,
    DocumentInfoT,
    ExternalTextCollectionT,
    StampT,
)
from iodd_parser.generated.v1_1.iodd_variables1_1 import VariableT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ErrorType128T(ErrorTypeT):
    code: int = field(
        init=False,
        default=128,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class IoddstandardEventCollectionT(CollectionT):
    class Meta:
        name = "IODDStandardEventCollectionT"

    event: list[EventDescT] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class IoddstandardVariableT(VariableT):
    class Meta:
        name = "IODDStandardVariableT"

    mandatory: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class UnitCollectionT(CollectionT):
    unit: list[UnitCollectionT.Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Unit:
        code: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        abbr: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        text_id: str = field(
            metadata={
                "name": "textId",
                "type": "Attribute",
                "required": True,
                "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
            }
        )


@dataclass(kw_only=True)
class IoddstandardErrorTypeCollectionT(CollectionT):
    class Meta:
        name = "IODDStandardErrorTypeCollectionT"

    error_type: list[ErrorType128T] = field(
        default_factory=list,
        metadata={
            "name": "ErrorType",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class IoddstandardUnitDefinitionsT:
    """
    :ivar document_info:
    :ivar unit_collection:
    :ivar external_text_collection:
    :ivar stamp: Filled out by the IODD Checker.
    """

    class Meta:
        name = "IODDStandardUnitDefinitionsT"

    document_info: DocumentInfoT = field(
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    unit_collection: UnitCollectionT = field(
        metadata={
            "name": "UnitCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    external_text_collection: ExternalTextCollectionT = field(
        metadata={
            "name": "ExternalTextCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    stamp: StampT = field(
        metadata={
            "name": "Stamp",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IoddstandardVariableCollectionT(CollectionT):
    class Meta:
        name = "IODDStandardVariableCollectionT"

    variable: list[IoddstandardVariableT] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class IoddstandardDefinitionsT:
    """
    :ivar document_info:
    :ivar datatype_collection:
    :ivar variable_collection:
    :ivar error_type_collection:
    :ivar event_collection:
    :ivar external_text_collection:
    :ivar stamp: Filled out by the IODD Checker.
    """

    class Meta:
        name = "IODDStandardDefinitionsT"

    document_info: DocumentInfoT = field(
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    datatype_collection: None | DatatypeCollectionT = field(
        default=None,
        metadata={
            "name": "DatatypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable_collection: IoddstandardVariableCollectionT = field(
        metadata={
            "name": "VariableCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    error_type_collection: IoddstandardErrorTypeCollectionT = field(
        metadata={
            "name": "ErrorTypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    event_collection: IoddstandardEventCollectionT = field(
        metadata={
            "name": "EventCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    external_text_collection: ExternalTextCollectionT = field(
        metadata={
            "name": "ExternalTextCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    stamp: StampT = field(
        metadata={
            "name": "Stamp",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IoddstandardUnitDefinitions(IoddstandardUnitDefinitionsT):
    class Meta:
        name = "IODDStandardUnitDefinitions"
        namespace = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IoddstandardDefinitions(IoddstandardDefinitionsT):
    class Meta:
        name = "IODDStandardDefinitions"
        namespace = "http://www.io-link.com/IODD/2010/10"
