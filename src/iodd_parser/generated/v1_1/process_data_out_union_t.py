from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.process_data_union_t import ProcessDataUnionT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataOutUnionT(ProcessDataUnionT):
    pass
