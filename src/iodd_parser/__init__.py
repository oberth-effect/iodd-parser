"""
IODD Parser package.

This package provides tools for parsing IO-Link Device Description (IODD)
files and resolving all references to produce unified data structures.
"""

from iodd_parser.parser import IODDParser
from iodd_parser.types import (
    IoddImage,
    ParsedIODD,
    ResolvedButton,
    ResolvedCondition,
    ResolvedError,
    ResolvedMenu,
    ResolvedMenuRef,
    ResolvedMenuSet,
    ResolvedProcessData,
    ResolvedProcessDataInfo,
    ResolvedProcessDataItem,
    ResolvedProcessDataRecordItemInfo,
    ResolvedProcessDataRef,
    ResolvedRecordItemRef,
    ResolvedUnit,
    ResolvedUserInterface,
    ResolvedVariable,
    ResolvedVariableRef,
    TopLevelMenuType,
    UserRole,
)

__all__ = [
    "IODDParser",
    "IoddImage",
    "ParsedIODD",
    "ResolvedButton",
    "ResolvedCondition",
    "ResolvedError",
    "ResolvedMenu",
    "ResolvedMenuRef",
    "ResolvedMenuSet",
    "ResolvedProcessData",
    "ResolvedProcessDataInfo",
    "ResolvedProcessDataItem",
    "ResolvedProcessDataRecordItemInfo",
    "ResolvedProcessDataRef",
    "ResolvedRecordItemRef",
    "ResolvedUnit",
    "ResolvedUserInterface",
    "ResolvedVariable",
    "ResolvedVariableRef",
    "TopLevelMenuType",
    "UserRole",
]
