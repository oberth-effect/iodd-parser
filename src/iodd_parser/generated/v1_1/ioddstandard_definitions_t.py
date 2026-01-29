from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_collection_t_1 import (
    DatatypeCollectionT1,
)
from iodd_parser.generated.v1_1.document_info_t_1 import DocumentInfoT1
from iodd_parser.generated.v1_1.external_text_collection_t_1 import (
    ExternalTextCollectionT1,
)
from iodd_parser.generated.v1_1.ioddstandard_error_type_collection_t import (
    IoddstandardErrorTypeCollectionT,
)
from iodd_parser.generated.v1_1.ioddstandard_event_collection_t import (
    IoddstandardEventCollectionT,
)
from iodd_parser.generated.v1_1.ioddstandard_variable_collection_t import (
    IoddstandardVariableCollectionT,
)
from iodd_parser.generated.v1_1.stamp_t import StampT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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

    document_info: DocumentInfoT1 = field(
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    datatype_collection: None | DatatypeCollectionT1 = field(
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
    external_text_collection: ExternalTextCollectionT1 = field(
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
