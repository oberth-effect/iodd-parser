from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.datatype_t_1 import DatatypeT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class SimpleDatatypeT1(DatatypeT1):
    class Meta:
        name = "SimpleDatatypeT"
