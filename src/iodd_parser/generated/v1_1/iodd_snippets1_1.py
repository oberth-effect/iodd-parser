from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from iodd_parser.generated.v1_1.xml import LangValue

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


class AccessRightsT(Enum):
    RO = "ro"
    RW = "rw"
    WO = "wo"


class CharacterEncodingT(Enum):
    UTF_8 = "UTF-8"
    US_ASCII = "US-ASCII"


@dataclass(kw_only=True)
class CollectionT:
    pass


@dataclass(kw_only=True)
class ConditionT:
    variable_id: str = field(
        metadata={
            "name": "variableId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    subindex: None | int | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    value: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


class ContextConstraintsT(Enum):
    IDENTIFICATION_MENU = "IdentificationMenu"
    PARAMETER_MENU = "ParameterMenu"
    OBSERVATION_MENU = "ObservationMenu"
    DIAGNOSIS_MENU = "DiagnosisMenu"


@dataclass(kw_only=True)
class DatatypeRefT:
    datatype_id: str = field(
        metadata={
            "name": "datatypeId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )


@dataclass(kw_only=True)
class DatatypeT:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class DocumentInfoT:
    """
    This type defines document information.
    """

    version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"V\d+(\.\d+){1,7}",
        }
    )
    release_date: str = field(
        metadata={
            "name": "releaseDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    copyright: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class EventDescTType(Enum):
    NOTIFICATION = "Notification"
    WARNING = "Warning"
    ERROR = "Error"


@dataclass(kw_only=True)
class FunctionClassT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    profile_id: int = field(
        metadata={
            "name": "profileId",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    profile_context: str = field(
        metadata={
            "name": "profileContext",
            "type": "Attribute",
            "required": True,
            "pattern": r"(\d+\.\.\d+|\d+)(, *(\d+\.\.\d+|\d+))*",
        }
    )


@dataclass(kw_only=True)
class ObjectT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )


@dataclass(kw_only=True)
class ProfileVariantT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    profile_id: int = field(
        metadata={
            "name": "profileId",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    profile_option: None | str = field(
        default=None,
        metadata={
            "name": "profileOption",
            "type": "Attribute",
            "pattern": r"(\d+( XOR \d+)+|\d+\.\.\d+|\d+)(, *(\d+( XOR \d+)+|\d+\.\.\d+|\d+))*",
        },
    )
    info: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RecordItemInfoT:
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class StdErrorTypeRefT:
    code: int = field(
        init=False,
        default=128,
        metadata={
            "type": "Attribute",
        },
    )
    additional_code: int = field(
        metadata={
            "name": "additionalCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StdEventRefT:
    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StdSingleValueRefT:
    value: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )


@dataclass(kw_only=True)
class TextDefinitionT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    value: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class TextRefT:
    text_id: str = field(
        metadata={
            "name": "textId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class UimenuRefSimpleT:
    class Meta:
        name = "UIMenuRefSimpleT"

    menu_id: str = field(
        metadata={
            "name": "menuId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class AbstractValueT:
    name: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )


@dataclass(kw_only=True)
class ButtonT:
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    action_started_message: None | TextRefT = field(
        default=None,
        metadata={
            "name": "ActionStartedMessage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    button_value: bool | int = field(
        metadata={
            "name": "buttonValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ComplexDatatypeT(DatatypeT):
    subindex_access_supported: bool = field(
        default=True,
        metadata={
            "name": "subindexAccessSupported",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DataItemT(ObjectT):
    datatype: None | DatatypeT = field(
        default=None,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    datatype_ref: None | DatatypeRefT = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )


@dataclass(kw_only=True)
class DatatypeCollectionT(CollectionT):
    datatype: list[DatatypeT] = field(
        default_factory=list,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ErrorTypeT:
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    additional_code: int = field(
        metadata={
            "name": "additionalCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EventDescT:
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    code: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: EventDescTType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LanguageT:
    text: list[TextDefinitionT] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    text_redefine: list[TextDefinitionT] = field(
        default_factory=list,
        metadata={
            "name": "TextRedefine",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    lang: str | LangValue = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class MenuSetT:
    identification_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "IdentificationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    parameter_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "ParameterMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    observation_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "ObservationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    diagnosis_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "DiagnosisMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class ProcessDataInfoT:
    gradient: None | Decimal | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    offset: None | Decimal | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    unit_code: None | int | str = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    display_format: None | object = field(
        default=None,
        metadata={
            "name": "displayFormat",
            "type": "Attribute",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )
    context_constraints: None | ContextConstraintsT = field(
        default=None,
        metadata={
            "name": "contextConstraints",
            "type": "Attribute",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )


@dataclass(kw_only=True)
class SimpleDatatypeT(DatatypeT):
    pass


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


@dataclass(kw_only=True)
class UimenuRefT(UimenuRefSimpleT):
    class Meta:
        name = "UIMenuRefT"

    condition: None | ConditionT = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )


@dataclass(kw_only=True)
class AbstractVariableT(DataItemT):
    record_item_info: list[RecordItemInfoT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    access_rights: AccessRightsT = field(
        metadata={
            "name": "accessRights",
            "type": "Attribute",
            "required": True,
        }
    )
    dynamic: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArrayT(ComplexDatatypeT):
    simple_datatype: None | SimpleDatatypeT = field(
        default=None,
        metadata={
            "name": "SimpleDatatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    datatype_ref: None | DatatypeRefT = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass(kw_only=True)
class ErrorType129T(ErrorTypeT):
    code: int = field(
        init=False,
        default=129,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EventCollectionT(CollectionT):
    std_event_ref: list[StdEventRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdEventRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    event: list[EventDescT] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class NumberT(SimpleDatatypeT):
    pass


@dataclass(kw_only=True)
class OctetStringT(SimpleDatatypeT):
    fixed_length: int | str = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class PrimaryLanguageT(LanguageT):
    pass


@dataclass(kw_only=True)
class ProcessDataItemT(DataItemT):
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    bit_length: object = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProcessDataRecordItemInfoT(ProcessDataInfoT):
    subindex: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class RecordItemT:
    simple_datatype: list[SimpleDatatypeT] = field(
        default_factory=list,
        metadata={
            "name": "SimpleDatatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
    datatype_ref: list[DatatypeRefT] = field(
        default_factory=list,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    subindex: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    bit_offset: object = field(
        metadata={
            "name": "bitOffset",
            "type": "Attribute",
            "required": True,
        }
    )
    access_right_restriction: None | AccessRightsT = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )


@dataclass(kw_only=True)
class SingleValueT(AbstractValueT):
    pass


@dataclass(kw_only=True)
class StringT(SimpleDatatypeT):
    fixed_length: int | str = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    encoding: CharacterEncodingT = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class UidataItemRefT(ProcessDataInfoT):
    class Meta:
        name = "UIDataItemRefT"

    button: None | ButtonT = field(
        default=None,
        metadata={
            "name": "Button",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable_id: str = field(
        metadata={
            "name": "variableId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    access_right_restriction: None | AccessRightsT = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ValueRangeT(AbstractValueT):
    pass


@dataclass(kw_only=True)
class BooleanValueT(SingleValueT):
    value: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ErrorTypeCollectionT(CollectionT):
    std_error_type_ref: list[StdErrorTypeRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdErrorTypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    error_type: list[ErrorType129T] = field(
        default_factory=list,
        metadata={
            "name": "ErrorType",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )


@dataclass(kw_only=True)
class ExternalTextCollectionT(CollectionT):
    primary_language: PrimaryLanguageT = field(
        metadata={
            "name": "PrimaryLanguage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    language: list[LanguageT] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )


@dataclass(kw_only=True)
class Float32ValueRangeT(ValueRangeT):
    lower_value: float | str = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    upper_value: float | str = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class Float32ValueT(SingleValueT):
    value: float | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class IntegerValueRangeT(ValueRangeT):
    lower_value: int | str = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    upper_value: int | str = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class IntegerValueT(SingleValueT):
    value: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class ProcessDataRefT:
    process_data_info: list[ProcessDataInfoT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )
    process_data_record_item_info: list[ProcessDataRecordItemInfoT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    process_data_id: str = field(
        metadata={
            "name": "processDataId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class ProcessDataT(ObjectT):
    condition: None | ConditionT = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    process_data_in: list[ProcessDataItemT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataIn",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    process_data_out: list[ProcessDataItemT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataOut",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )


@dataclass(kw_only=True)
class RecordT(ComplexDatatypeT):
    record_item: list[RecordItemT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItem",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
    bit_length: object = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StdDataItemRefT:
    std_single_value_ref: list[StdSingleValueRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdSingleValueRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    single_value: list[StdDataItemRefT.SingleValue] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[StdDataItemRefT.ValueRange] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
    check_attributes: None | str = field(
        default=None,
        metadata={
            "name": "checkAttributes",
            "type": "Attribute",
            "pattern": r"((option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)(, +(option|startsWith|notEmpty) +[a-z][0-9A-Za-z]*)*",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )

    @dataclass(kw_only=True)
    class SingleValue(SingleValueT):
        value: object = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ValueRange(ValueRangeT):
        lower_value: object = field(
            metadata={
                "name": "lowerValue",
                "type": "Attribute",
                "required": True,
            }
        )
        upper_value: object = field(
            metadata={
                "name": "upperValue",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class TbdValueRangeT(ValueRangeT):
    lower_value: object = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
        }
    )
    upper_value: object = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TbdValueT(SingleValueT):
    value: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class UirecordItemRefT(UidataItemRefT):
    class Meta:
        name = "UIRecordItemRefT"

    subindex: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class UivariableRefT(UidataItemRefT):
    class Meta:
        name = "UIVariableRefT"


@dataclass(kw_only=True)
class UintegerValueRangeT(ValueRangeT):
    class Meta:
        name = "UIntegerValueRangeT"

    lower_value: int | str = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )
    upper_value: int | str = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class UintegerValueT(SingleValueT):
    class Meta:
        name = "UIntegerValueT"

    value: int | str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        }
    )


@dataclass(kw_only=True)
class VariableT(AbstractVariableT):
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BooleanT(SimpleDatatypeT):
    single_value: list[BooleanValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Float32T(NumberT):
    single_value: list[Float32ValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[Float32ValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )


@dataclass(kw_only=True)
class IntegerT(NumberT):
    single_value: list[IntegerValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[IntegerValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 64,
        }
    )


@dataclass(kw_only=True)
class MenuT:
    name: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable_ref: list[UivariableRefT] = field(
        default_factory=list,
        metadata={
            "name": "VariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    record_item_ref: list[UirecordItemRefT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    menu_ref: list[UimenuRefT] = field(
        default_factory=list,
        metadata={
            "name": "MenuRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    context_constraints: None | ContextConstraintsT = field(
        default=None,
        metadata={
            "name": "contextConstraints",
            "type": "Attribute",
        },
    )
    profile_constraints: None | str = field(
        default=None,
        metadata={
            "name": "profileConstraints",
            "type": "Attribute",
            "pattern": r"(PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?(, (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+)( AND (PR_[A-Za-z0-9]+|FC_[A-Za-z0-9]+))?)*",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class ProcessDataCollectionT(CollectionT):
    process_data: list[ProcessDataT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessData",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class ProcessDataRefCollectionT:
    process_data_ref: list[ProcessDataRefT] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDataRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class StdRecordItemRefT(StdDataItemRefT):
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass(kw_only=True)
class UintegerT(NumberT):
    class Meta:
        name = "UIntegerT"

    single_value: list[UintegerValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[UintegerValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 64,
        }
    )


@dataclass(kw_only=True)
class AnyType(NumberT):
    class Meta:
        name = "any"

    single_value: list[TbdValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    value_range: list[TbdValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    bit_length: None | int = field(
        default=None,
        metadata={
            "name": "bitLength",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MenuCollectionT(CollectionT):
    menu: list[MenuT] = field(
        default_factory=list,
        metadata={
            "name": "Menu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "min_occurs": 1,
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class StdVariableRefT(StdDataItemRefT):
    std_record_item_ref: list[StdRecordItemRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdRecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*(#tbd#)?|#tbd#",
        }
    )
    fixed_length_restriction: None | int | str = field(
        default=None,
        metadata={
            "name": "fixedLengthRestriction",
            "type": "Attribute",
            "min_inclusive": 1,
            "pattern": r"#tbd(#| ?(-?\d+\.\.-?\d+|-?\d+)(, *(-?\d+\.\.-?\d+|-?\d+))* ?#)",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class UserInterfaceT:
    process_data_ref_collection: None | ProcessDataRefCollectionT = field(
        default=None,
        metadata={
            "name": "ProcessDataRefCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    menu_collection: MenuCollectionT = field(
        metadata={
            "name": "MenuCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    observer_role_menu_set: MenuSetT = field(
        metadata={
            "name": "ObserverRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    maintenance_role_menu_set: MenuSetT = field(
        metadata={
            "name": "MaintenanceRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    specialist_role_menu_set: MenuSetT = field(
        metadata={
            "name": "SpecialistRoleMenuSet",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )


@dataclass(kw_only=True)
class VariableCollectionT(CollectionT):
    std_variable_ref: list[StdVariableRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdVariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable: list[VariableCollectionT.Variable] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )

    @dataclass(kw_only=True)
    class Variable(VariableT):
        default_value: None | object = field(
            default=None,
            metadata={
                "name": "defaultValue",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class IoddprofileDefinitionsT:
    class Meta:
        name = "IODDProfileDefinitionsT"

    document_info: DocumentInfoT = field(
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
    datatype_collection: None | DatatypeCollectionT = field(
        default=None,
        metadata={
            "name": "DatatypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    variable_collection: VariableCollectionT = field(
        metadata={
            "name": "VariableCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    process_data_collection: None | ProcessDataCollectionT = field(
        default=None,
        metadata={
            "name": "ProcessDataCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    error_type_collection: None | ErrorTypeCollectionT = field(
        default=None,
        metadata={
            "name": "ErrorTypeCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    event_collection: None | EventCollectionT = field(
        default=None,
        metadata={
            "name": "EventCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    user_interface: UserInterfaceT = field(
        metadata={
            "name": "UserInterface",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    external_text_collection: ExternalTextCollectionT = field(
        metadata={
            "name": "ExternalTextCollection",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IoddprofileDefinitions(IoddprofileDefinitionsT):
    class Meta:
        name = "IODDProfileDefinitions"
        namespace = "http://www.io-link.com/IODD-Snippets/2025/10"
