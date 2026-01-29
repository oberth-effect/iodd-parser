from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.function_class_t import FunctionClassT
from iodd_parser.generated.v1_1.profile_variant_t import ProfileVariantT

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class SupportedProfilesT:
    profile_variant: list[ProfileVariantT] = field(
        default_factory=list,
        metadata={
            "name": "ProfileVariant",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    function_class: list[FunctionClassT] = field(
        default_factory=list,
        metadata={
            "name": "FunctionClass",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    profile_characteristic: str = field(
        metadata={
            "name": "profileCharacteristic",
            "type": "Attribute",
            "required": True,
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        }
    )
    profile_class_name: None | str = field(
        default=None,
        metadata={
            "name": "profileClassName",
            "type": "Attribute",
        },
    )
    profile_prefixes: None | str = field(
        default=None,
        metadata={
            "name": "profilePrefixes",
            "type": "Attribute",
            "pattern": r"([A-Za-z][A-Za-z0-9 _-]*)(, +[A-Za-z][A-Za-z0-9 _-]*)*",
        },
    )
    reserved_index_range: None | str = field(
        default=None,
        metadata={
            "name": "reservedIndexRange",
            "type": "Attribute",
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        },
    )
    reserved_system_commands: None | str = field(
        default=None,
        metadata={
            "name": "reservedSystemCommands",
            "type": "Attribute",
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        },
    )
    reserved_events: None | str = field(
        default=None,
        metadata={
            "name": "reservedEvents",
            "type": "Attribute",
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        },
    )
    required_profile: None | str = field(
        default=None,
        metadata={
            "name": "requiredProfile",
            "type": "Attribute",
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        },
    )
