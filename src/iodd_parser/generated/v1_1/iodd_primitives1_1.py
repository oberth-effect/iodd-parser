from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from iodd_parser.generated.v1_1.xml import LangValue

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    subindex: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    value: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
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


@dataclass(kw_only=True)
class ObjectT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )


@dataclass(kw_only=True)
class StampT:
    checker: StampT.Checker = field(
        metadata={
            "name": "Checker",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    crc: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Checker:
        name: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        version: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"V\d+(\.\d+){1,7}",
            }
        )


@dataclass(kw_only=True)
class TextDefinitionT:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    value: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TextRefT:
    text_id: str = field(
        metadata={
            "name": "textId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )


@dataclass(kw_only=True)
class LanguageT:
    text: list[TextDefinitionT] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    text_redefine: list[TextDefinitionT] = field(
        default_factory=list,
        metadata={
            "name": "TextRedefine",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    lang: str | LangValue = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ExternalTextDocumentT:
    """
    This type defines the structure of the file that contains external
    language dependent text definitions.

    One file can contain texts of only one language.

    :ivar document_info:
    :ivar language:
    :ivar stamp: Filled out by the IODD Checker.
    """

    document_info: None | DocumentInfoT = field(
        default=None,
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    language: LanguageT = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    stamp: StampT = field(
        metadata={
            "name": "Stamp",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PrimaryLanguageT(LanguageT):
    pass


@dataclass(kw_only=True)
class ExternalTextCollectionT(CollectionT):
    primary_language: PrimaryLanguageT = field(
        metadata={
            "name": "PrimaryLanguage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    language: list[LanguageT] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class ExternalTextDocument(ExternalTextDocumentT):
    """
    This defines the root element of the file that contains external text
    definitions.
    """

    class Meta:
        namespace = "http://www.io-link.com/IODD/2010/10"
