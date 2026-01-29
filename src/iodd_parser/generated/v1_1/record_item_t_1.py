from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.access_rights_t_1 import AccessRightsT1
from iodd_parser.generated.v1_1.datatype_ref_t_1 import DatatypeRefT1
from iodd_parser.generated.v1_1.simple_datatype_t_1 import SimpleDatatypeT1
from iodd_parser.generated.v1_1.text_ref_t_1 import TextRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class RecordItemT1:
    class Meta:
        name = "RecordItemT"

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
    name: TextRefT1 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT1 = field(
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
    access_right_restriction: None | AccessRightsT1 = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )
