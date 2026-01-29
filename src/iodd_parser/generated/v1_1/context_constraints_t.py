from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


class ContextConstraintsT(Enum):
    IDENTIFICATION_MENU = "IdentificationMenu"
    PARAMETER_MENU = "ParameterMenu"
    OBSERVATION_MENU = "ObservationMenu"
    DIAGNOSIS_MENU = "DiagnosisMenu"
