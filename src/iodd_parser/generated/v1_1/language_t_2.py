from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.lang_value import LangValue
from iodd_parser.generated.v1_1.text_definition_t_2 import TextDefinitionT2

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class LanguageT2:
    class Meta:
        name = "LanguageT"

    text: list[TextDefinitionT2] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    text_redefine: list[TextDefinitionT2] = field(
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
