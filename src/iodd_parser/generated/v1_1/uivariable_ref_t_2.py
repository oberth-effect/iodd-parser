from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.uidata_item_ref_t_2 import UidataItemRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class UivariableRefT2(UidataItemRefT2):
    class Meta:
        name = "UIVariableRefT"
