from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_t_1 import DatatypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ComplexDatatypeT1(DatatypeT1):
    class Meta:
        name = "ComplexDatatypeT"

    subindex_access_supported: bool = field(
        default=True,
        metadata={
            "name": "subindexAccessSupported",
            "type": "Attribute",
        },
    )
