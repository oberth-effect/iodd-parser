from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.complex_datatype_t import ComplexDatatypeT
from iodd_parser.generated.v1_1.datatype_ref_t import DatatypeRefT
from iodd_parser.generated.v1_1.simple_datatype_t import SimpleDatatypeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ArrayT(ComplexDatatypeT):
    simple_datatype: None | SimpleDatatypeT = field(
        default=None,
        metadata={
            "name": "SimpleDatatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    datatype_ref: None | DatatypeRefT = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
