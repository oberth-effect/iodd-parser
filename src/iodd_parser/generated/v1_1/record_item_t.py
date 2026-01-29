from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t import AccessRightsT
from iodd_parser.generated.v1_1.datatype_ref_t import DatatypeRefT
from iodd_parser.generated.v1_1.simple_datatype_t import SimpleDatatypeT
from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class RecordItemT:
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
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    bit_offset: int = field(
        metadata={
            "name": "bitOffset",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 1855,
        }
    )
    access_right_restriction: None | AccessRightsT = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )
