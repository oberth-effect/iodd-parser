from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_1 import CollectionT1
from iodd_parser.generated.v1_1.language_t_1 import LanguageT1
from iodd_parser.generated.v1_1.primary_language_t_1 import PrimaryLanguageT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ExternalTextCollectionT1(CollectionT1):
    class Meta:
        name = "ExternalTextCollectionT"

    primary_language: PrimaryLanguageT1 = field(
        metadata={
            "name": "PrimaryLanguage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    language: list[LanguageT1] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
