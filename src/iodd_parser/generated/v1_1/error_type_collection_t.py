from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t import CollectionT
from iodd_parser.generated.v1_1.error_type129_t import ErrorType129T
from iodd_parser.generated.v1_1.std_error_type_ref_t import StdErrorTypeRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
