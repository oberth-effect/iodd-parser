from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.error_type128_t import ErrorType128T

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IoddstandardErrorTypeCollectionT(CollectionT1):
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
