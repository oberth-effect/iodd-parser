from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.ioddprofile_definitions_t import (
    IoddprofileDefinitionsT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class IoddprofileDefinitions(IoddprofileDefinitionsT):
    class Meta:
        name = "IODDProfileDefinitions"
        namespace = "http://www.io-link.com/IODD-Snippets/2025/10"
