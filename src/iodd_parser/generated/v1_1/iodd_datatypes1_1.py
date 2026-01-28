from __future__ import annotations

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1.iodd_primitives1_1 import (
    AccessRightsT,
    CharacterEncodingT,
    CollectionT,
    TextRefT,
)

__NAMESPACE__ = "http://www.io-link.com/IODD/2010/10"


@dataclass(kw_only=True)
class DatatypeRefT:
    datatype_id: str = field(
        metadata={
            "name": "datatypeId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        }
    )


@dataclass(kw_only=True)
class DatatypeT:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z][A-Za-z0-9 _-]*[A-Za-z0-9]",
        },
    )


@dataclass(kw_only=True)
class AbstractValueT:
    name: None | TextRefT = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class ComplexDatatypeT(DatatypeT):
    subindex_access_supported: bool = field(
        default=True,
        metadata={
            "name": "subindexAccessSupported",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DatatypeCollectionT(CollectionT):
    datatype: list[DatatypeT] = field(
        default_factory=list,
        metadata={
            "name": "Datatype",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ProcessDataUnionT(DatatypeT):
    """
    This datatype is a union of all process data definitions.

    Thus the size equals the size of the largest process data definition.
    """


@dataclass(kw_only=True)
class SimpleDatatypeT(DatatypeT):
    pass


@dataclass(kw_only=True)
class ArrayT(ComplexDatatypeT):
    simple_datatype: None | SimpleDatatypeT = field(
        default=None,
        metadata={
            "name": "SimpleDatatype",
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
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass(kw_only=True)
class NumberT(SimpleDatatypeT):
    pass


@dataclass(kw_only=True)
class OctetStringT(SimpleDatatypeT):
    fixed_length: int = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
        }
    )


@dataclass(kw_only=True)
class ProcessDataInUnionT(ProcessDataUnionT):
    pass


@dataclass(kw_only=True)
class ProcessDataOutUnionT(ProcessDataUnionT):
    pass


@dataclass(kw_only=True)
class RecordItemT:
    simple_datatype: None | SimpleDatatypeT = field(
        default=None,
        metadata={
            "name": "SimpleDatatype",
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
    subindex: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    bit_offset: int = field(
        metadata={
            "name": "bitOffset",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 1855,
        }
    )
    access_right_restriction: None | AccessRightsT = field(
        default=None,
        metadata={
            "name": "accessRightRestriction",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SingleValueT(AbstractValueT):
    pass


@dataclass(kw_only=True)
class StringT(SimpleDatatypeT):
    fixed_length: int = field(
        metadata={
            "name": "fixedLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 232,
        }
    )
    encoding: CharacterEncodingT = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TimeSpanT(SimpleDatatypeT):
    pass


@dataclass(kw_only=True)
class TimeT(SimpleDatatypeT):
    pass


@dataclass(kw_only=True)
class ValueRangeT(AbstractValueT):
    pass


@dataclass(kw_only=True)
class BooleanValueT(SingleValueT):
    value: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Float32ValueRangeT(ValueRangeT):
    lower_value: float = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
        }
    )
    upper_value: float = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Float32ValueT(SingleValueT):
    value: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IntegerValueRangeT(ValueRangeT):
    lower_value: int = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
        }
    )
    upper_value: int = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class IntegerValueT(SingleValueT):
    value: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RecordT(ComplexDatatypeT):
    record_item: list[RecordItemT] = field(
        default_factory=list,
        metadata={
            "name": "RecordItem",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "min_occurs": 1,
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 1856,
        }
    )


@dataclass(kw_only=True)
class UintegerValueRangeT(ValueRangeT):
    class Meta:
        name = "UIntegerValueRangeT"

    lower_value: int = field(
        metadata={
            "name": "lowerValue",
            "type": "Attribute",
            "required": True,
        }
    )
    upper_value: int = field(
        metadata={
            "name": "upperValue",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class UintegerValueT(SingleValueT):
    class Meta:
        name = "UIntegerValueT"

    value: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BooleanT(SimpleDatatypeT):
    single_value: list[BooleanValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Float32T(NumberT):
    single_value: list[Float32ValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[Float32ValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )


@dataclass(kw_only=True)
class IntegerT(NumberT):
    single_value: list[IntegerValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[IntegerValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 64,
        }
    )


@dataclass(kw_only=True)
class UintegerT(NumberT):
    class Meta:
        name = "UIntegerT"

    single_value: list[UintegerValueT] = field(
        default_factory=list,
        metadata={
            "name": "SingleValue",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    value_range: list[UintegerValueRangeT] = field(
        default_factory=list,
        metadata={
            "name": "ValueRange",
            "type": "Element",
            "namespace": "http://www.io-link.com/IODD/2010/10",
        },
    )
    bit_length: int = field(
        metadata={
            "name": "bitLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 64,
        }
    )
