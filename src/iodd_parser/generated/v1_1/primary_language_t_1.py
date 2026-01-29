from __future__ import annotations

from dataclasses import dataclass

from iodd_parser.generated.v1_1.language_t_1 import LanguageT1

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class PrimaryLanguageT1(LanguageT1):
    class Meta:
        name = "PrimaryLanguageT"
