from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


class AccessRightsT2(Enum):
    RO = "ro"
    RW = "rw"
    WO = "wo"
