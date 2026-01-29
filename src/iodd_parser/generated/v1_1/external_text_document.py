from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.external_text_document_t import (
    ExternalTextDocumentT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class ExternalTextDocument(ExternalTextDocumentT):
    """
    This defines the root element of the file that contains external text
    definitions.
    """

    class Meta:
        namespace = "http://www.io-link.com/IODD/2010/10"
