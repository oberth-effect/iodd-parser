from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_collection_t import (
    DatatypeCollectionT,
)
from iodd_parser.generated.v1_1.error_type_collection_t import (
    ErrorTypeCollectionT,
)
from iodd_parser.generated.v1_1.event_collection_t import EventCollectionT
from iodd_parser.generated.v1_1.features_t import FeaturesT
from iodd_parser.generated.v1_1.process_data_collection_t import (
    ProcessDataCollectionT,
)
from iodd_parser.generated.v1_1.user_interface_t import UserInterfaceT
from iodd_parser.generated.v1_1.variable_collection_t import (
    VariableCollectionT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
