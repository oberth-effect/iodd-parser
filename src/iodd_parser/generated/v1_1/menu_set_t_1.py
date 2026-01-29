from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.uimenu_ref_simple_t_1 import UimenuRefSimpleT1

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


@dataclass(kw_only=True)
class MenuSetT1:
    class Meta:
        name = "MenuSetT"

    identification_menu: None | UimenuRefSimpleT1 = field(
        default=None,
        metadata={
            "name": "IdentificationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    parameter_menu: None | UimenuRefSimpleT1 = field(
        default=None,
        metadata={
            "name": "ParameterMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    observation_menu: None | UimenuRefSimpleT1 = field(
        default=None,
        metadata={
            "name": "ObservationMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    diagnosis_menu: None | UimenuRefSimpleT1 = field(
        default=None,
        metadata={
            "name": "DiagnosisMenu",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD-Snippets/2025/10",
        },
    )
    check_element: None | str = field(
        default=None,
        metadata={
            "name": "checkElement",
            "type": "Attribute",
            "pattern": r"((minOccurs +\d+|maxOccurs +\d+)(, (exact|atLeast|atLeastSequence))?)|(exact|atLeast|atLeastSequence)",
        },
    )
