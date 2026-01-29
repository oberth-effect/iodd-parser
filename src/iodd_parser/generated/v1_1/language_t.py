from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.lang_value import LangValue
from iodd_parser.generated.v1_1.text_definition_t import TextDefinitionT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


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
