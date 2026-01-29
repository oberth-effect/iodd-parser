from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.complex_datatype_t_1 import ComplexDatatypeT1
from iodd_parser.generated.v1_1.datatype_ref_t_1 import DatatypeRefT1
from iodd_parser.generated.v1_1.simple_datatype_t_1 import SimpleDatatypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ArrayT1(ComplexDatatypeT1):
    class Meta:
        name = "ArrayT"

    simple_datatype: None | SimpleDatatypeT1 = field(
        default=None,
        metadata={
            "name": "SimpleDatatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    datatype_ref: None | DatatypeRefT1 = field(
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
