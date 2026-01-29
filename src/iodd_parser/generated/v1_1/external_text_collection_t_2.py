from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.collection_t_2 import CollectionT2
from iodd_parser.generated.v1_1.language_t_2 import LanguageT2
from iodd_parser.generated.v1_1.primary_language_t_2 import PrimaryLanguageT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class ExternalTextCollectionT2(CollectionT2):
    class Meta:
        name = "ExternalTextCollectionT"

    primary_language: PrimaryLanguageT2 = field(
        metadata={
            "name": "PrimaryLanguage",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
            "required": True,
        }
    )
    language: list[LanguageT2] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
