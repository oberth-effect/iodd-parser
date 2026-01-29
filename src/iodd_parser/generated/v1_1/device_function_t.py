from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_collection_t_1 import (
    DatatypeCollectionT1,
)
from iodd_parser.generated.v1_1.error_type_collection_t_1 import (
    ErrorTypeCollectionT1,
)
from iodd_parser.generated.v1_1.event_collection_t_1 import EventCollectionT1
from iodd_parser.generated.v1_1.features_t import FeaturesT
from iodd_parser.generated.v1_1.process_data_collection_t_2 import (
    ProcessDataCollectionT2,
)
from iodd_parser.generated.v1_1.user_interface_t_2 import UserInterfaceT2
from iodd_parser.generated.v1_1.variable_collection_t_2 import (
    VariableCollectionT2,
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
    datatype_collection: None | DatatypeCollectionT1 = field(
        default=None,
        metadata={
            "name": "DatatypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable_collection: VariableCollectionT2 = field(
        metadata={
            "name": "VariableCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    process_data_collection: ProcessDataCollectionT2 = field(
        metadata={
            "name": "ProcessDataCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    error_type_collection: None | ErrorTypeCollectionT1 = field(
        default=None,
        metadata={
            "name": "ErrorTypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    event_collection: None | EventCollectionT1 = field(
        default=None,
        metadata={
            "name": "EventCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    user_interface: UserInterfaceT2 = field(
        metadata={
            "name": "UserInterface",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
