from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from iodd_parser.generated.v1_1.iodd_communication1_1 import (
    CommNetworkProfileT,
)
from iodd_parser.generated.v1_1.iodd_datatypes1_1 import DatatypeCollectionT
from iodd_parser.generated.v1_1.iodd_events1_1 import (
    ErrorTypeCollectionT,
    EventCollectionT,
)
from iodd_parser.generated.v1_1.iodd_primitives1_1 import (
    CollectionT,
    ConditionT,
    DocumentInfoT,
    ExternalTextCollectionT,
    ObjectT,
    StampT,
    TextRefT,
)
from iodd_parser.generated.v1_1.iodd_user_interface1_1 import UserInterfaceT
from iodd_parser.generated.v1_1.iodd_variables1_1 import (
    DataItemT,
    VariableCollectionT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


class ProfileHeaderTProfileClassId(Enum):
    DEVICE = "Device"


class ProfileHeaderTProfileIdentification(Enum):
    IO_DEVICE_PROFILE = "IO Device Profile"


class ProfileHeaderTProfileName(Enum):
    DEVICE_PROFILE_FOR_IO_DEVICES = "Device Profile for IO Devices"


class ProfileHeaderTProfileRevision(Enum):
    VALUE_1_1 = "1.1"


class ProfileHeaderTProfileSource(Enum):
    IO_LINK_CONSORTIUM = "IO-Link Consortium"


@dataclass(kw_only=True)
class SupportedAccessLocksT:
    parameter: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    data_storage: bool = field(
        metadata={
            "name": "dataStorage",
            "type": "Attribute",
            "required": True,
        }
    )
    local_parameterization: bool = field(
        metadata={
            "name": "localParameterization",
            "type": "Attribute",
            "required": True,
        }
    )
    local_user_interface: bool = field(
        metadata={
            "name": "localUserInterface",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DeviceVariantT:
    """
    :ivar name:
    :ivar description:
    :ivar product_id: This must be the same product ID as returned by
        the corresponding IO-Link index. This ensures unique
        identification of the device during scanning.
    :ivar device_symbol: The symbol shall be available as PNG, 160x160
        pixels. The filename must not have a path prefix and shall
        follow the naming rules.
    :ivar device_icon: The icon shall be available as PNG, 48x48 pixels.
        The filename must not have a path prefix and shall follow the
        naming rules.
    """

    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: TextRefT = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    product_id: str = field(
        metadata={
            "name": "productId",
            "type": "Attribute",
            "required": True,
        }
    )
    device_symbol: None | str = field(
        default=None,
        metadata={
            "name": "deviceSymbol",
            "type": "Attribute",
            "pattern": r"([\p{L}\d_#]+-)+pic\.png",
        },
    )
    device_icon: None | str = field(
        default=None,
        metadata={
            "name": "deviceIcon",
            "type": "Attribute",
            "pattern": r"([\p{L}\d_#]+-)+icon\.png",
        },
    )


@dataclass(kw_only=True)
class FeaturesT:
    supported_access_locks: None | SupportedAccessLocksT = field(
        default=None,
        metadata={
            "name": "SupportedAccessLocks",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    block_parameter: bool = field(
        metadata={
            "name": "blockParameter",
            "type": "Attribute",
            "required": True,
        }
    )
    data_storage: bool = field(
        metadata={
            "name": "dataStorage",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_characteristic: list[int] = field(
        default_factory=list,
        metadata={
            "name": "profileCharacteristic",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ProcessDataItemT(DataItemT):
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 256,
        }
    )


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


@dataclass(kw_only=True)
class DeviceVariantCollectionT(CollectionT):
    device_variant: list[DeviceVariantT] = field(
        default_factory=list,
        metadata={
            "name": "DeviceVariant",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


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


@dataclass(kw_only=True)
class DeviceIdentityT:
    """
    :ivar vendor_text:
    :ivar vendor_url:
    :ivar vendor_logo: This logo shall be available as PNG, 160x90
        pixels. The filename must not have a path prefix and shall
        follow the naming rules.
    :ivar device_name:
    :ivar device_family:
    :ivar device_variant_collection:
    :ivar vendor_id:
    :ivar vendor_name:
    :ivar device_id:
    :ivar additional_device_ids:
    """

    vendor_text: TextRefT = field(
        metadata={
            "name": "VendorText",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    vendor_url: TextRefT = field(
        metadata={
            "name": "VendorUrl",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    vendor_logo: None | DeviceIdentityT.VendorLogo = field(
        default=None,
        metadata={
            "name": "VendorLogo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    device_name: TextRefT = field(
        metadata={
            "name": "DeviceName",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    device_family: TextRefT = field(
        metadata={
            "name": "DeviceFamily",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    device_variant_collection: DeviceVariantCollectionT = field(
        metadata={
            "name": "DeviceVariantCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    vendor_id: int = field(
        metadata={
            "name": "vendorId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    vendor_name: str = field(
        metadata={
            "name": "vendorName",
            "type": "Attribute",
            "required": True,
        }
    )
    device_id: int = field(
        metadata={
            "name": "deviceId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 16777215,
        }
    )
    additional_device_ids: list[int] = field(
        default_factory=list,
        metadata={
            "name": "additionalDeviceIds",
            "type": "Attribute",
            "min_inclusive": 1,
            "min_length": 1,
            "max_inclusive": 16777215,
            "max_length": 255,
            "tokens": True,
        },
    )

    @dataclass(kw_only=True)
    class VendorLogo:
        name: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"([\p{L}\d_#]+-)+logo\.png",
            }
        )


@dataclass(kw_only=True)
class ProcessDataCollectionT(CollectionT):
    process_data: list[ProcessDataT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessData",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DeviceFunctionT:
    """
    :ivar features:
    :ivar datatype_collection:
    :ivar variable_collection: Simple collection of all variables
        supported by the device.
    :ivar process_data_collection:
    :ivar error_type_collection:
    :ivar event_collection:
    :ivar user_interface:
    """

    features: FeaturesT = field(
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    datatype_collection: None | DatatypeCollectionT = field(
        default=None,
        metadata={
            "name": "DatatypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable_collection: VariableCollectionT = field(
        metadata={
            "name": "VariableCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    process_data_collection: ProcessDataCollectionT = field(
        metadata={
            "name": "ProcessDataCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    error_type_collection: None | ErrorTypeCollectionT = field(
        default=None,
        metadata={
            "name": "ErrorTypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    event_collection: None | EventCollectionT = field(
        default=None,
        metadata={
            "name": "EventCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    user_interface: UserInterfaceT = field(
        metadata={
            "name": "UserInterface",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProfileBodyT:
    device_identity: DeviceIdentityT = field(
        metadata={
            "name": "DeviceIdentity",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    device_function: DeviceFunctionT = field(
        metadata={
            "name": "DeviceFunction",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Iodevice:
    """
    :ivar document_info:
    :ivar profile_header:
    :ivar profile_body:
    :ivar comm_network_profile:
    :ivar external_text_collection:
    :ivar stamp: Filled out by the IODD Checker.
    """

    class Meta:
        name = "IODevice"
        namespace = "http://www.io-link.com/IODD/2010/10"

    document_info: DocumentInfoT = field(
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "required": True,
        }
    )
    profile_header: ProfileHeaderT = field(
        metadata={
            "name": "ProfileHeader",
            "type": "Element",
            "required": True,
        }
    )
    profile_body: ProfileBodyT = field(
        metadata={
            "name": "ProfileBody",
            "type": "Element",
            "required": True,
        }
    )
    comm_network_profile: CommNetworkProfileT = field(
        metadata={
            "name": "CommNetworkProfile",
            "type": "Element",
            "required": True,
        }
    )
    external_text_collection: ExternalTextCollectionT = field(
        metadata={
            "name": "ExternalTextCollection",
            "type": "Element",
            "required": True,
        }
    )
    stamp: StampT = field(
        metadata={
            "name": "Stamp",
            "type": "Element",
            "required": True,
        }
    )
