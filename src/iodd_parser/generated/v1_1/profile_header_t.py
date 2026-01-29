from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.profile_header_t_profile_class_id import (
    ProfileHeaderTProfileClassId,
)
from iodd_parser.generated.v1_1.profile_header_t_profile_identification import (
    ProfileHeaderTProfileIdentification,
)
from iodd_parser.generated.v1_1.profile_header_t_profile_name import (
    ProfileHeaderTProfileName,
)
from iodd_parser.generated.v1_1.profile_header_t_profile_revision import (
    ProfileHeaderTProfileRevision,
)
from iodd_parser.generated.v1_1.profile_header_t_profile_source import (
    ProfileHeaderTProfileSource,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ProfileHeaderT:
    profile_identification: ProfileHeaderTProfileIdentification = field(
        metadata={
            "name": "ProfileIdentification",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    profile_revision: ProfileHeaderTProfileRevision = field(
        metadata={
            "name": "ProfileRevision",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    profile_name: ProfileHeaderTProfileName = field(
        metadata={
            "name": "ProfileName",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    profile_source: ProfileHeaderTProfileSource = field(
        metadata={
            "name": "ProfileSource",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    profile_class_id: ProfileHeaderTProfileClassId = field(
        metadata={
            "name": "ProfileClassID",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    iso15745_reference: ProfileHeaderT.Iso15745Reference = field(
        metadata={
            "name": "ISO15745Reference",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Iso15745Reference:
        iso15745_part: int = field(
            init=False,
            default=1,
            metadata={
                "name": "ISO15745Part",
                "type": "Element",
                "namespace": "http://www.io-link.com/IODD/2010/10",
                "required": True,
            },
        )
        iso15745_edition: int = field(
            init=False,
            default=1,
            metadata={
                "name": "ISO15745Edition",
                "type": "Element",
                "namespace": "http://www.io-link.com/IODD/2010/10",
                "required": True,
            },
        )
        profile_technology: str = field(
            init=False,
            default="IODD",
            metadata={
                "name": "ProfileTechnology",
                "type": "Element",
                "namespace": "http://www.io-link.com/IODD/2010/10",
                "required": True,
            },
        )
