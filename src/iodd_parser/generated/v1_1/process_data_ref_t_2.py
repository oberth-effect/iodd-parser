from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.process_data_info_t_2 import ProcessDataInfoT2
from iodd_parser.generated.v1_1.process_data_record_item_info_t_2 import (
    ProcessDataRecordItemInfoT2,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataRefT2:
    class Meta:
        name = "ProcessDataRefT"

    process_data_info: None | ProcessDataInfoT2 = field(
        default=None,
        metadata={
            "name": "ProcessDataInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_record_item_info: list[ProcessDataRecordItemInfoT2] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_id: str = field(
        metadata={
            "name": "processDataId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
