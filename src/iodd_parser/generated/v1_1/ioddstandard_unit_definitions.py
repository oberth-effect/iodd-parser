from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.ioddstandard_unit_definitions_t import (
    IoddstandardUnitDefinitionsT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IoddstandardUnitDefinitions(IoddstandardUnitDefinitionsT):
    class Meta:
        name = "IODDStandardUnitDefinitions"
        namespace = "http://www.io-link.com/IODD/2010/10"
