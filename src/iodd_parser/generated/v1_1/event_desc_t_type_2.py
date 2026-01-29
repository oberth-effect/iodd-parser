from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.io-link.com/IODD-Snippets/2025/10"


class EventDescTType2(Enum):
    NOTIFICATION = "Notification"
    WARNING = "Warning"
    ERROR = "Error"
