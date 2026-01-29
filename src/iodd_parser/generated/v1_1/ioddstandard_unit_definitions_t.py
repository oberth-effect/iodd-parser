from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.document_info_t_1 import DocumentInfoT1
from iodd_parser.generated.v1_1.external_text_collection_t_1 import (
    ExternalTextCollectionT1,
)
from iodd_parser.generated.v1_1.stamp_t import StampT
from iodd_parser.generated.v1_1.unit_collection_t import UnitCollectionT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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

    document_info: DocumentInfoT1 = field(
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
