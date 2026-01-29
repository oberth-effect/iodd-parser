from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


class AccessRightsT1(Enum):
    RO = "ro"
    RW = "rw"
    WO = "wo"
