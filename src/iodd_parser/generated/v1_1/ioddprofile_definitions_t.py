from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.datatype_collection_t_2 import (
    DatatypeCollectionT2,
)
from iodd_parser.generated.v1_1.document_info_t_2 import DocumentInfoT2
from iodd_parser.generated.v1_1.error_type_collection_t_2 import (
    ErrorTypeCollectionT2,
)
from iodd_parser.generated.v1_1.event_collection_t_2 import EventCollectionT2
from iodd_parser.generated.v1_1.external_text_collection_t_2 import (
    ExternalTextCollectionT2,
)
from iodd_parser.generated.v1_1.process_data_collection_t_1 import (
    ProcessDataCollectionT1,
)
from iodd_parser.generated.v1_1.supported_profiles_t import SupportedProfilesT
from iodd_parser.generated.v1_1.user_interface_t_1 import UserInterfaceT1
from iodd_parser.generated.v1_1.variable_collection_t_1 import (
    VariableCollectionT1,
)

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class IoddprofileDefinitionsT:
    class Meta:
        name = "IODDProfileDefinitionsT"

    document_info: DocumentInfoT2 = field(
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    supported_profiles: SupportedProfilesT = field(
        metadata={
            "name": "SupportedProfiles",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    datatype_collection: None | DatatypeCollectionT2 = field(
        default=None,
        metadata={
            "name": "DatatypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable_collection: VariableCollectionT1 = field(
        metadata={
            "name": "VariableCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    process_data_collection: None | ProcessDataCollectionT1 = field(
        default=None,
        metadata={
            "name": "ProcessDataCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    error_type_collection: None | ErrorTypeCollectionT2 = field(
        default=None,
        metadata={
            "name": "ErrorTypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    event_collection: None | EventCollectionT2 = field(
        default=None,
        metadata={
            "name": "EventCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    user_interface: UserInterfaceT1 = field(
        metadata={
            "name": "UserInterface",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    external_text_collection: ExternalTextCollectionT2 = field(
        metadata={
            "name": "ExternalTextCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
