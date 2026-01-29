from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


class WireFunctionT(Enum):
    NC = "NC"
    L = "L+"
    L_1 = "L-"
    P24 = "P24"
    N24 = "N24"
    OTHER = "Other"
    C_Q = "C/Q"
