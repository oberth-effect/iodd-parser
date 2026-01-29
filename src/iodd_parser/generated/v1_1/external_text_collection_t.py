from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t import CollectionT
from iodd_parser.generated.v1_1.language_t import LanguageT
from iodd_parser.generated.v1_1.primary_language_t import PrimaryLanguageT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
