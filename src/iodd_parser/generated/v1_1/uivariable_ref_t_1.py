from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.uidata_item_ref_t_1 import UidataItemRefT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class UivariableRefT1(UidataItemRefT1):
    class Meta:
        name = "UIVariableRefT"
