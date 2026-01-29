from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.document_info_t import DocumentInfoT
from iodd_parser.generated.v1_1.language_t import LanguageT
from iodd_parser.generated.v1_1.stamp_t import StampT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
