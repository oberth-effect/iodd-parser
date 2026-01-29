from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.abstract_value_t_2 import AbstractValueT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ValueRangeT2(AbstractValueT2):
    class Meta:
        name = "ValueRangeT"
