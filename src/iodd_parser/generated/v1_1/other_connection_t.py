from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.connection_t import ConnectionT
from iodd_parser.generated.v1_1.text_ref_t import TextRefT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class OtherConnectionT(ConnectionT):
    description: TextRefT = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
