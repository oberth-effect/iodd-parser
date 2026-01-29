from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.condition_t_1 import ConditionT1
from iodd_parser.generated.v1_1.object_t_1 import ObjectT1
from iodd_parser.generated.v1_1.process_data_item_t_2 import ProcessDataItemT2

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProcessDataT2(ObjectT1):
    class Meta:
        name = "ProcessDataT"

    condition: None | ConditionT1 = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_in: None | ProcessDataItemT2 = field(
        default=None,
        metadata={
            "name": "ProcessDataIn",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    process_data_out: None | ProcessDataItemT2 = field(
        default=None,
        metadata={
            "name": "ProcessDataOut",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
