from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.process_data_info_t_1 import ProcessDataInfoT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ProcessDataRecordItemInfoT1(ProcessDataInfoT1):
    class Meta:
        name = "ProcessDataRecordItemInfoT"

    subindex: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
