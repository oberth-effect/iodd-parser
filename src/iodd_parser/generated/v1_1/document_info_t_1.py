from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DocumentInfoT1:
    """
    This type defines document information.
    """

    class Meta:
        name = "DocumentInfoT"

    version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"V\d+(\.\d+){1,7}",
        }
    )
    release_date: str = field(
        metadata={
            "name": "releaseDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    copyright: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
