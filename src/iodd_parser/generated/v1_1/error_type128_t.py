from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.error_type_t import ErrorTypeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ErrorType128T(ErrorTypeT):
    code: int = field(
        init=False,
        default=128,
        metadata={
            "type": "Attribute",
        },
    )
