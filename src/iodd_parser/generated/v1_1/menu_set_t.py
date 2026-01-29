from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.uimenu_ref_simple_t import UimenuRefSimpleT

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class MenuSetT:
    identification_menu: UimenuRefSimpleT = field(
        metadata={
            "name": "IdentificationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    parameter_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "ParameterMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    observation_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "ObservationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    diagnosis_menu: None | UimenuRefSimpleT = field(
        default=None,
        metadata={
            "name": "DiagnosisMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
