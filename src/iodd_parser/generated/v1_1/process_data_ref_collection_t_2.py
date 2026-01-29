from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.process_data_ref_t_2 import ProcessDataRefT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataRefCollectionT2:
    class Meta:
        name = "ProcessDataRefCollectionT"

    process_data_ref: list[ProcessDataRefT2] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
