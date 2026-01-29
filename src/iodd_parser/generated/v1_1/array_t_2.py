from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.complex_datatype_t_2 import ComplexDatatypeT2
from iodd_parser.generated.v1_1.datatype_ref_t_2 import DatatypeRefT2
from iodd_parser.generated.v1_1.simple_datatype_t_2 import SimpleDatatypeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ArrayT2(ComplexDatatypeT2):
    class Meta:
        name = "ArrayT"

    simple_datatype: None | SimpleDatatypeT2 = field(
        default=None,
        metadata={
            "name": "SimpleDatatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    datatype_ref: None | DatatypeRefT2 = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
