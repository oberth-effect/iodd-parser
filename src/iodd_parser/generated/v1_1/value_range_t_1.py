from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.abstract_value_t_1 import AbstractValueT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ValueRangeT1(AbstractValueT1):
    class Meta:
        name = "ValueRangeT"
