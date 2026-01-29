from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.datatype_t import DatatypeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class SimpleDatatypeT(DatatypeT):
    pass
