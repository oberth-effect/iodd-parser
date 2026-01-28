from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iodd_datatypes1_1 import (
    DatatypeRefT,
    DatatypeT,
    SingleValueT,
    ValueRangeT,
)
from iodd_parser.generated.v1_1.iodd_primitives1_1 import (
    AccessRightsT,
    CollectionT,
    ObjectT,
    TextRefT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class RecordItemInfoT:
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class StdSingleValueRefT:
    value: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DataItemT(ObjectT):
    datatype: None | DatatypeT = field(
        default=None,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    datatype_ref: None | DatatypeRefT = field(
        default=None,
        metadata={
            "name": "DatatypeRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class StdDataItemRefT:
    std_single_value_ref: list[StdSingleValueRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdSingleValueRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    single_value: list[StdDataItemRefT.SingleValue] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[StdDataItemRefT.ValueRange] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    default_value: None | object = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class SingleValue(SingleValueT):
        value: object = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ValueRange(ValueRangeT):
        lower_value: object = field(
            metadata={
                "name": "lowerValue",
                "type": "Attribute",
                "required": True,
            }
        )
        upper_value: object = field(
            metadata={
                "name": "upperValue",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class AbstractVariableT(DataItemT):
    record_item_info: list[RecordItemInfoT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItemInfo",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    name: TextRefT = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "required": True,
        }
    )
    description: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    access_rights: AccessRightsT = field(
        metadata={
            "name": "accessRights",
            "type": "Attribute",
            "required": True,
        }
    )
    dynamic: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    modifies_other_variables: bool = field(
        default=False,
        metadata={
            "name": "modifiesOtherVariables",
            "type": "Attribute",
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class StdRecordItemRefT(StdDataItemRefT):
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass(kw_only=True)
class StdVariableRefT(StdDataItemRefT):
    std_record_item_ref: list[StdRecordItemRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdRecordItemRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )
    fixed_length_restriction: None | int = field(
        default=None,
        metadata={
            "name": "fixedLengthRestriction",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    excluded_from_data_storage: bool = field(
        default=False,
        metadata={
            "name": "excludedFromDataStorage",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class VariableT(AbstractVariableT):
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class VariableCollectionT(CollectionT):
    std_variable_ref: list[StdVariableRefT] = field(
        default_factory=list,
        metadata={
            "name": "StdVariableRef",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 2,
        },
    )
    direct_parameter_overlay: None | AbstractVariableT = field(
        default=None,
        metadata={
            "name": "DirectParameterOverlay",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    variable: list[VariableCollectionT.Variable] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )

    @dataclass(kw_only=True)
    class Variable(VariableT):
        default_value: None | object = field(
            default=None,
            metadata={
                "name": "defaultValue",
                "type": "Attribute",
            },
        )
