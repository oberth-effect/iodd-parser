from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ErrorTypeT:
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
    code: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    additional_code: int = field(
        metadata={
            "name": "additionalCode",
            "type": "Attribute",
            "required": True,
        }
    )
