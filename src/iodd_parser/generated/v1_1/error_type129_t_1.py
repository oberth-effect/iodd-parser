from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.error_type_t_1 import ErrorTypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ErrorType129T1(ErrorTypeT1):
    class Meta:
        name = "ErrorType129T"

    code: int = field(
        init=False,
        default=129,
        metadata={
            "type": "Attribute",
        },
    )
