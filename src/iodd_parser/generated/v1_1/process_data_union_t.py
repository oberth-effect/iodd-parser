from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.datatype_t import DatatypeT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataUnionT(DatatypeT):
    """
    This datatype is a union of all process data definitions.

    Thus the size equals the size of the largest process data definition.
    """
