from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.condition_t import ConditionT
from iodd_parser.generated.v1_1.object_t import ObjectT
from iodd_parser.generated.v1_1.process_data_item_t import ProcessDataItemT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataT(ObjectT):
    condition: None | ConditionT = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_in: None | ProcessDataItemT = field(
        default=None,
        metadata={
            "name": "ProcessDataIn",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_out: None | ProcessDataItemT = field(
        default=None,
        metadata={
            "name": "ProcessDataOut",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
