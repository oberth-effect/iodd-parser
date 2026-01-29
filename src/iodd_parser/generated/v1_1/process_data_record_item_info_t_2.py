from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.process_data_info_t_2 import ProcessDataInfoT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataRecordItemInfoT2(ProcessDataInfoT2):
    class Meta:
        name = "ProcessDataRecordItemInfoT"

    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
