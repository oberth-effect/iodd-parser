from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iolink_test_config7_t import IolinkTestConfig7T
from iodd_parser.generated.v1_1.iolink_test_config_t import IolinkTestConfigT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class IolinkTestT:
    class Meta:
        name = "IOLinkTestT"

    config1: None | IolinkTestConfigT = field(
        default=None,
        metadata={
            "name": "Config1",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    config2: None | IolinkTestConfigT = field(
        default=None,
        metadata={
            "name": "Config2",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    config3: None | IolinkTestConfigT = field(
        default=None,
        metadata={
            "name": "Config3",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    config7: None | IolinkTestConfig7T = field(
        default=None,
        metadata={
            "name": "Config7",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
