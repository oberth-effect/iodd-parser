from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_2 import CollectionT2
from iodd_parser.generated.v1_1.error_type129_t_2 import ErrorType129T2
from iodd_parser.generated.v1_1.std_error_type_ref_t_2 import StdErrorTypeRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ErrorTypeCollectionT2(CollectionT2):
    class Meta:
        name = "ErrorTypeCollectionT"

    std_error_type_ref: list[StdErrorTypeRefT2] = field(
        default_factory=list,
        metadata={
            "name": "StdErrorTypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    error_type: list[ErrorType129T2] = field(
        default_factory=list,
        metadata={
            "name": "ErrorType",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
