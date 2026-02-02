"""
Type definitions for parsed IODD data.

This module contains dataclass definitions for resolved IODD elements
with all references resolved to their actual values.
"""

from dataclasses import dataclass, field

from iodd_parser.generated.v1_1 import (
    AccessRightsT,
    DatatypeT,
    IoddstandardDefinitions,
    IoddstandardUnitDefinitions,
    Iodevice,
    RecordItemInfoT,
    TextRefT,
)


@dataclass
class IoddImage:
    """
    An image extracted from an IODD zip archive.

    :ivar filename: The filename of the image within the archive.
    :ivar data: The raw binary data of the image.
    """

    filename: str
    data: bytes


@dataclass
class ResolvedVariable:
    """
    A resolved variable with all references resolved.

    Variables can come from three sources:

    - **StdVariableRef**: references to standard variables from
      the loaded Standard Definitions file.
    - **DirectParameterOverlay**: device-specific data within DirectParameter page
    - **Variable**: vendor-specific variables with a device-specific index

    :ivar id: Unique identifier of the variable within the IODD.
    :ivar index: Index for addressing the variable (ISDU index).
    :ivar datatype: The resolved data type of the variable.
    :ivar name: The resolved human-readable name.
    :ivar description: The resolved description text, if available.
    :ivar access_rights: Access rights (read-only, write-only, read-write).
    :ivar dynamic: Whether the variable is autonomously changed by the device.
    :ivar modifies_other_variables: Whether writing to this variable may change
        other variables.
    :ivar excluded_from_data_storage: Whether the variable is excluded from
        data storage mechanism.
    :ivar default_value: The offline default value, if specified.
    :ivar fixed_length_restriction: Length restriction for string/array types.
    :ivar record_item_info: Additional information for record items.
    """

    id: str
    index: int
    datatype: None | DatatypeT
    name: str
    description: None | str
    access_rights: AccessRightsT
    dynamic: bool
    modifies_other_variables: bool
    excluded_from_data_storage: bool
    default_value: None | object = None
    fixed_length_restriction: None | int = None
    record_item_info: list[RecordItemInfoT] = field(default_factory=list)


@dataclass
class ResolvedError:
    """
    A resolved error type with all references resolved.

    Error types are identified by a combination of code and additional_code:

    - **code=128**: Standard errors from the loaded Standard Definitions file.
    - **code=129**: Vendor-specific errors defined in the device IODD

    :ivar code: The error code (128 for standard, 129 for vendor-specific).
    :ivar additional_code: The additional code identifying the specific error.
    :ivar name: The resolved error message text.
    :ivar description: The resolved description (cause and remedy), if available.
    """

    code: int
    additional_code: int
    name: str
    description: None | str


@dataclass
class ResolvedUnit:
    """
    A resolved unit with its code, abbreviation, and name.

    Units are defined in IODD-StandardUnitDefinitions1.1.xml.

    :ivar code: The unit code (e.g., 1001 for degrees Celsius).
    :ivar abbreviation: The short form (e.g., "°C").
    :ivar name: The full name (e.g., "degree Celsius").
    """

    code: int
    abbreviation: str
    name: str


@dataclass
class ResolvedProcessDataItem:
    """
    A resolved process data item (input or output).

    ProcessDataIn/ProcessDataOut elements describe the structure of
    the cyclic process data exchanged between master and device.

    :ivar id: Explicit id of the ProcessDataIn/ProcessDataOut description.
    :ivar bit_length: Length of the process data in bits (1..256).
    :ivar name: The resolved name of the process data.
    :ivar datatype: The data type (directly given or resolved from DatatypeRef).
    """

    id: str
    bit_length: int
    name: str
    datatype: None | DatatypeT = None


@dataclass
class ResolvedProcessData:
    """
    Resolved process data with optional condition for switching.

    ProcessData elements can have a Condition element that allows switching
    between different process data configurations based on a variable value.
    Multiple ProcessData elements may exist when conditional switching is used.

    :ivar id: Explicit id of the ProcessData.
    :ivar process_data_in: Description of input process data (device to master).
    :ivar process_data_out: Description of output process data (master to device).
    :ivar condition_variable_id: Variable id for switching, if conditional.
    :ivar condition_subindex: Subindex for record item addressing, if applicable.
    :ivar condition_value: The value that selects this ProcessData configuration.
    """

    id: str
    process_data_in: None | ResolvedProcessDataItem = None
    process_data_out: None | ResolvedProcessDataItem = None
    condition_variable_id: None | str = None
    condition_subindex: None | int = None
    condition_value: None | int = None


@dataclass
class ParsedIODD:
    """
    The result of parsing an IODD file with all references resolved.

    This dataclass contains both the raw parsed IODD objects and
    resolved/processed data for convenient access.

    :ivar iodd_definitions: The parsed standard definitions XML.
    :ivar iodd_units: The parsed standard unit definitions XML.
    :ivar iodd_device: The parsed device IODD XML.
    :ivar device_name: The resolved device name.
    :ivar device_manufacturer: The vendor/manufacturer name.
    :ivar variables: Dict of resolved variables, keyed by variable id.
    :ivar process_data: Dict of resolved process data, keyed by id.
    :ivar texts: Dict of all text strings, keyed by text id.
    :ivar datatypes: Dict of all data types, keyed by datatype id.
    :ivar errors: Dict of resolved errors, keyed by (code, additional_code).
    :ivar units: Dict of resolved units, keyed by unit code.
    :ivar images: List of images extracted from the IODD archive.
    """

    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice

    device_name: str
    device_manufacturer: str
    variables: dict[str, ResolvedVariable]
    process_data: dict[str, ResolvedProcessData]
    texts: dict[str, str]
    datatypes: dict[str, DatatypeT]
    errors: dict[tuple[int, int], ResolvedError]
    units: dict[int, ResolvedUnit]

    images: list[IoddImage]

    def get_text(self, ref: TextRefT) -> str | None:
        """
        Get the text string for a text reference.

        :param ref: The text reference object containing the text_id.
        :returns: The resolved text string, or None if not found.
        """
        return self.texts.get(ref.text_id)
