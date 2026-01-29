from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.simple_datatype_t_2 import SimpleDatatypeT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class NumberT2(SimpleDatatypeT2):
    class Meta:
        name = "NumberT"
