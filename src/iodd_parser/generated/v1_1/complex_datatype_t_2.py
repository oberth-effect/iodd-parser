from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_t_2 import DatatypeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ComplexDatatypeT2(DatatypeT2):
    class Meta:
        name = "ComplexDatatypeT"

    subindex_access_supported: bool = field(
        default=True,
        metadata={
            "name": "subindexAccessSupported",
            "type": "Attribute",
        },
    )
