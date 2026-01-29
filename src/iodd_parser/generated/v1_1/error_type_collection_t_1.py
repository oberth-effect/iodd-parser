from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.error_type129_t_1 import ErrorType129T1
from iodd_parser.generated.v1_1.std_error_type_ref_t_1 import StdErrorTypeRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ErrorTypeCollectionT1(CollectionT1):
    class Meta:
        name = "ErrorTypeCollectionT"

    std_error_type_ref: list[StdErrorTypeRefT1] = field(
        default_factory=list,
        metadata={
            "name": "StdErrorTypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    error_type: list[ErrorType129T1] = field(
        default_factory=list,
        metadata={
            "name": "ErrorType",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
