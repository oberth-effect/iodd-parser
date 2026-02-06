"""
Type definitions for parsed IODD data.

This module contains dataclass definitions for resolved IODD elements
with all references resolved to their actual values.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from iodd_parser.generated.v1_1 import (
    AccessRightsT,
    CharacterEncodingT,
    DatatypeT,
    IoddstandardDefinitions,
    IoddstandardUnitDefinitions,
    Iodevice,
    RecordItemInfoT,
    TextRefT,
)


class UserRole(Enum):
    """
    User roles for the device user interface.

    :cvar OBSERVER: Operator role - read-only access, no modifications allowed.
    :cvar MAINTENANCE: Maintenance role - uncritical editing allowed.
    :cvar SPECIALIST: Specialist role - full access to the device.
    """

    OBSERVER = "observer"
    MAINTENANCE = "maintenance"
    SPECIALIST = "specialist"


class TopLevelMenuType(Enum):
    """
    Types of top-level menus in a role menu set.

    :cvar IDENTIFICATION: Menu for device identification variables.
    :cvar PARAMETER: Menu for device parameterization variables.
    :cvar OBSERVATION: Menu for observation (process data, dynamic variables).
    :cvar DIAGNOSIS: Menu for diagnosis (events, etc.).
    """

    IDENTIFICATION = "identification"
    PARAMETER = "parameter"
    OBSERVATION = "observation"
    DIAGNOSIS = "diagnosis"


# =============================================================================
# Resolved Datatype Classes
# =============================================================================


@dataclass
class ResolvedSingleValue:
    """
    A resolved single value with name text resolved.

    SingleValue defines a named value for numeric types (UIntegerT, IntegerT,
    Float32T) or boolean types. The name provides a human-readable label for
    the value.

    :ivar value: The actual value (int, float, or bool depending on type).
    :ivar name: The resolved name text for this value, if specified.
    """

    value: int | float | bool
    name: str | None = None


@dataclass
class ResolvedValueRange:
    """
    A resolved value range with name text resolved.

    ValueRange defines a valid range of values for numeric types.

    :ivar lower_value: The inclusive lower bound of the range.
    :ivar upper_value: The inclusive upper bound of the range.
    :ivar name: The resolved name text for this range, if specified.
    """

    lower_value: int | float
    upper_value: int | float
    name: str | None = None


@dataclass
class ResolvedUIntegerT:
    """
    A resolved unsigned integer datatype.

    :ivar bit_length: The bit length of the integer (2-64).
    :ivar single_values: List of named single values.
    :ivar value_ranges: List of valid value ranges.
    """

    bit_length: int
    single_values: list[ResolvedSingleValue] = field(default_factory=list)
    value_ranges: list[ResolvedValueRange] = field(default_factory=list)


@dataclass
class ResolvedIntegerT:
    """
    A resolved signed integer datatype.

    :ivar bit_length: The bit length of the integer (2-64).
    :ivar single_values: List of named single values.
    :ivar value_ranges: List of valid value ranges.
    """

    bit_length: int
    single_values: list[ResolvedSingleValue] = field(default_factory=list)
    value_ranges: list[ResolvedValueRange] = field(default_factory=list)


@dataclass
class ResolvedFloat32T:
    """
    A resolved 32-bit float datatype.

    :ivar single_values: List of named single values.
    :ivar value_ranges: List of valid value ranges.
    """

    single_values: list[ResolvedSingleValue] = field(default_factory=list)
    value_ranges: list[ResolvedValueRange] = field(default_factory=list)


@dataclass
class ResolvedBooleanT:
    """
    A resolved boolean datatype.

    :ivar single_values: List of named single values (typically for true/false).
    """

    single_values: list[ResolvedSingleValue] = field(default_factory=list)


@dataclass
class ResolvedStringT:
    """
    A resolved string datatype.

    :ivar fixed_length: The fixed length of the string (1-232 characters).
    :ivar encoding: The character encoding (ASCII or UTF-8).
    """

    fixed_length: int
    encoding: CharacterEncodingT


@dataclass
class ResolvedOctetStringT:
    """
    A resolved octet string (byte array) datatype.

    :ivar fixed_length: The fixed length in octets (1-232).
    """

    fixed_length: int


@dataclass
class ResolvedTimeT:
    """
    A resolved time datatype (absolute timestamp).

    Represents a point in time as yyyy-mm-dd hh:mm:ss.fff
    """

    pass


@dataclass
class ResolvedTimeSpanT:
    """
    A resolved time span datatype (duration).

    Represents a duration as [+-][d ]hh:mm:ss.fff
    """

    pass


@dataclass
class ResolvedRecordItemT:
    """
    A resolved record item within a record datatype.

    :ivar subindex: The subindex of this item within the record.
    :ivar bit_offset: The bit offset within the record.
    :ivar name: The resolved name of the record item.
    :ivar description: The resolved description, if available.
    :ivar datatype: The resolved datatype of this record item.
    """

    subindex: int
    bit_offset: int
    name: str
    description: str | None
    datatype: (
        ResolvedUIntegerT
        | ResolvedIntegerT
        | ResolvedFloat32T
        | ResolvedBooleanT
        | ResolvedStringT
        | ResolvedOctetStringT
        | ResolvedTimeT
        | ResolvedTimeSpanT
        | ResolvedRecordT
        | ResolvedArrayT
        | None
    )


@dataclass
class ResolvedRecordT:
    """
    A resolved record (struct) datatype.

    :ivar bit_length: The total bit length of the record.
    :ivar subindex_access_supported: Whether individual items can be accessed by subindex.
    :ivar items: List of record items in order.
    """

    bit_length: int
    subindex_access_supported: bool
    items: list[ResolvedRecordItemT] = field(default_factory=list)


@dataclass
class ResolvedArrayT:
    """
    A resolved array datatype.

    :ivar count: The number of elements in the array.
    :ivar subindex_access_supported: Whether individual elements can be accessed by subindex.
    :ivar element_datatype: The resolved datatype of array elements.
    """

    count: int
    subindex_access_supported: bool
    element_datatype: (
        ResolvedUIntegerT
        | ResolvedIntegerT
        | ResolvedFloat32T
        | ResolvedBooleanT
        | ResolvedStringT
        | ResolvedOctetStringT
        | ResolvedTimeT
        | ResolvedTimeSpanT
        | ResolvedRecordT
        | ResolvedArrayT
        | None
    )


# Union type for all resolved datatypes
ResolvedDatatype = (
    ResolvedUIntegerT
    | ResolvedIntegerT
    | ResolvedFloat32T
    | ResolvedBooleanT
    | ResolvedStringT
    | ResolvedOctetStringT
    | ResolvedTimeT
    | ResolvedTimeSpanT
    | ResolvedRecordT
    | ResolvedArrayT
    | None
)


# =============================================================================
# UI and Menu Types
# =============================================================================


@dataclass
class ResolvedButton:
    """
    A resolved button for command interface.

    Buttons are used to implement command interfaces to the device.
    When pressed, the button value is immediately sent to the device.

    :ivar button_value: The value sent to the device when the button is clicked.
    :ivar description: A text explaining the action started by pressing the button.
    :ivar action_started_message: A text shown after the value was successfully sent.
    """

    button_value: bool | int
    description: str | None = None
    action_started_message: str | None = None


@dataclass
class ResolvedVariableRef:
    """
    A resolved variable reference in a menu.

    Defines how a variable should be displayed in the user interface,
    with optional gradient/offset transformations and display formatting.

    :ivar variable_id: The referenced variable id.
    :ivar gradient: Gradient for value transformation (displayed = value * gradient + offset).
    :ivar offset: Offset for value transformation.
    :ivar unit_code: Unit code for the displayed value.
    :ivar display_format: Display format (Bin, Hex, Dec, Dec.x).
    :ivar access_right_restriction: Access rights restriction for certain user roles.
    :ivar button: Button definition if this variable ref displays as a button.
    """

    variable_id: str
    gradient: Decimal | None = None
    offset: Decimal | None = None
    unit_code: int | None = None
    display_format: str | None = None
    access_right_restriction: AccessRightsT | None = None
    button: ResolvedButton | None = None


@dataclass
class ResolvedRecordItemRef:
    """
    A resolved record item reference in a menu.

    Like VariableRef but addresses a specific record item via subindex.
    The referenced variable must be of type record.

    :ivar variable_id: The referenced variable id (must be of type record).
    :ivar subindex: The subindex addressing the record item within the record.
    :ivar gradient: Gradient for value transformation.
    :ivar offset: Offset for value transformation.
    :ivar unit_code: Unit code for the displayed value.
    :ivar display_format: Display format (Bin, Hex, Dec, Dec.x).
    :ivar access_right_restriction: Access rights restriction for certain user roles.
    :ivar button: Button definition if this record item ref displays as a button.
    """

    variable_id: str
    subindex: int
    gradient: Decimal | None = None
    offset: Decimal | None = None
    unit_code: int | None = None
    display_format: str | None = None
    access_right_restriction: AccessRightsT | None = None
    button: ResolvedButton | None = None


@dataclass
class ResolvedCondition:
    """
    A resolved condition for conditional menu display.

    An IO-Link Tool shows the referenced menu only if the value of the
    referenced variable/record item equals the condition value.

    :ivar variable_id: The referenced condition variable id.
    :ivar subindex: Subindex for record item addressing (if variable is RecordT).
    :ivar value: The value that must match for the condition to be true (0-255).
    """

    variable_id: str
    subindex: int | None
    value: int


@dataclass
class ResolvedMenuRef:
    """
    A resolved reference to a sub-menu.

    :ivar menu_id: The referenced menu id from the MenuCollection.
    :ivar condition: Optional condition for conditional display of this menu.
    """

    menu_id: str
    condition: ResolvedCondition | None = None


@dataclass
class ResolvedMenu:
    """
    A resolved menu from the MenuCollection.

    A menu contains references to variables, record items, and sub-menus.
    Items are displayed in the order they appear in the IODD.

    :ivar id: Explicit id of the menu.
    :ivar name: The resolved menu name (may be None for top-level menus).
    :ivar variable_refs: List of variable references in this menu.
    :ivar record_item_refs: List of record item references in this menu.
    :ivar menu_refs: List of sub-menu references in this menu.
    """

    id: str
    name: str | None
    variable_refs: list[ResolvedVariableRef] = field(default_factory=list)
    record_item_refs: list[ResolvedRecordItemRef] = field(default_factory=list)
    menu_refs: list[ResolvedMenuRef] = field(default_factory=list)


@dataclass
class ResolvedProcessDataRecordItemInfo:
    """
    Display info for a record item within process data.

    :ivar subindex: The subindex of the record item.
    :ivar gradient: Gradient for value transformation.
    :ivar offset: Offset for value transformation.
    :ivar unit_code: Unit code for the displayed value.
    :ivar display_format: Display format (Bin, Hex, Dec, Dec.x).
    """

    subindex: int
    gradient: Decimal | None = None
    offset: Decimal | None = None
    unit_code: int | None = None
    display_format: str | None = None


@dataclass
class ResolvedProcessDataInfo:
    """
    Display info for process data (non-record type).

    :ivar gradient: Gradient for value transformation.
    :ivar offset: Offset for value transformation.
    :ivar unit_code: Unit code for the displayed value.
    :ivar display_format: Display format (Bin, Hex, Dec, Dec.x).
    """

    gradient: Decimal | None = None
    offset: Decimal | None = None
    unit_code: int | None = None
    display_format: str | None = None


@dataclass
class ResolvedProcessDataRef:
    """
    A resolved reference to process data with display info.

    Defines how process data should be displayed in the user interface.

    :ivar process_data_id: Reference to ProcessDataIn or ProcessDataOut id.
    :ivar process_data_info: Display info for non-record process data.
    :ivar record_item_infos: Display info for record items (for record-type process data).
    """

    process_data_id: str
    process_data_info: ResolvedProcessDataInfo | None = None
    record_item_infos: list[ResolvedProcessDataRecordItemInfo] = field(default_factory=list)


@dataclass
class ResolvedMenuSet:
    """
    A resolved role menu set with top-level menu references.

    Each role has a set of fixed top-level menus. The menu names are
    hard-coded by tools and should not be taken from the IODD.

    :ivar identification_menu_id: Menu id for device identification (mandatory).
    :ivar parameter_menu_id: Menu id for device parameters (optional).
    :ivar observation_menu_id: Menu id for observation/process data (optional).
    :ivar diagnosis_menu_id: Menu id for diagnosis/events (optional).
    """

    identification_menu_id: str
    parameter_menu_id: str | None = None
    observation_menu_id: str | None = None
    diagnosis_menu_id: str | None = None


@dataclass
class ResolvedUserInterface:
    """
    A resolved user interface with all menus and role assignments.

    The user interface defines how the device is presented in IO-Link Tools,
    organized by user roles with hierarchical menus.

    :ivar menus: Dict of all menus, keyed by menu id.
    :ivar observer_role_menu_set: Menu set for the Observer (Operator) role.
    :ivar maintenance_role_menu_set: Menu set for the Maintenance role.
    :ivar specialist_role_menu_set: Menu set for the Specialist role.
    :ivar process_data_refs: List of process data display references.
    """

    menus: dict[str, ResolvedMenu]
    observer_role_menu_set: ResolvedMenuSet
    maintenance_role_menu_set: ResolvedMenuSet
    specialist_role_menu_set: ResolvedMenuSet
    process_data_refs: list[ResolvedProcessDataRef] = field(default_factory=list)


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
    datatype: ResolvedDatatype
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
    :ivar datatype: The resolved data type.
    """

    id: str
    bit_length: int
    name: str
    datatype: ResolvedDatatype = None


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
    The result of parsing an IODD file before reference resolution.

    This dataclass contains the raw parsed IODD XML objects and
    language-specific texts. Use the :meth:`resolve` method to produce
    a fully resolved :class:`ResolvedIODD` object.

    :ivar iodd_definitions: The parsed standard definitions XML.
    :ivar iodd_units: The parsed standard unit definitions XML.
    :ivar iodd_device: The parsed device IODD XML.
    :ivar standard_lang_texts: Dict of language code to text dictionaries from
        standard definitions.
    :ivar device_lang_texts: Dict of language code to text dictionaries from
        device-specific language files.
    :ivar images: List of images extracted from the IODD archive.
    """

    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice
    standard_lang_texts: dict[str, dict[str, str]]
    device_lang_texts: dict[str, dict[str, str]]
    images: list[IoddImage]

    @property
    def available_languages(self) -> set[str]:
        """
        Get the set of available language codes.

        :returns: A set of language codes available in either standard or device texts.
        """
        return set(self.standard_lang_texts.keys()) | set(self.device_lang_texts.keys())

    def resolve(self, lang: str | None = None) -> ResolvedIODD:
        """
        Resolve all references and produce a fully resolved ResolvedIODD object.

        This method resolves all text references, datatypes, variables, errors,
        units, process data, and user interface elements.

        :param lang: Optional language code (e.g., "de", "fr") for localised texts.
            When specified, texts are resolved in the following priority order
            (later sources override earlier ones):

            1. Primary language (English) from standard definitions
            2. Primary language from device IODD
            3. Primary language from standard unit definitions (English only)
            4. Pre-loaded language-specific standard definitions file (if available)
            5. Language sections within main standard definitions file
            6. Language sections within main device IODD file
            7. Device-specific language file (e.g., ``*-IODD1.1-de.xml``) - highest priority

        :returns: A :class:`ResolvedIODD` object with all references resolved.
        """
        # Import here to avoid circular imports
        from iodd_parser.resolvers import (
            resolve_errors,
            resolve_process_data,
            resolve_texts,
            resolve_units,
            resolve_user_interface,
            resolve_variables,
        )

        texts = resolve_texts(
            self.iodd_definitions,
            self.iodd_units,
            self.iodd_device,
            lang,
            self.standard_lang_texts,
            self.device_lang_texts,
        )

        # Build datatypes lookup from both standard definitions and device
        datatypes: dict[str, DatatypeT] = {}
        if self.iodd_definitions.datatype_collection is not None:
            for dt in self.iodd_definitions.datatype_collection.datatype:
                if dt.id is not None:
                    datatypes[dt.id] = dt
        if self.iodd_device.profile_body.device_function.datatype_collection is not None:
            for dt in self.iodd_device.profile_body.device_function.datatype_collection.datatype:
                if dt.id is not None:
                    datatypes[dt.id] = dt

        # Resolve all collections
        errors = resolve_errors(
            self.iodd_definitions.error_type_collection,
            self.iodd_device.profile_body.device_function.error_type_collection,
            texts,
        )

        units = resolve_units(self.iodd_units, texts)

        variables = resolve_variables(
            self.iodd_definitions.variable_collection,
            self.iodd_device.profile_body.device_function.variable_collection,
            texts,
            datatypes,
        )

        process_data = resolve_process_data(
            self.iodd_device.profile_body.device_function.process_data_collection,
            texts,
            datatypes,
        )

        user_interface = resolve_user_interface(
            self.iodd_device.profile_body.device_function.user_interface,
            texts,
        )

        # Extract device identity information
        device_identity = self.iodd_device.profile_body.device_identity
        device_name = texts.get(
            device_identity.device_name.text_id,
            device_identity.device_name.text_id,
        )

        return ResolvedIODD(
            iodd_definitions=self.iodd_definitions,
            iodd_units=self.iodd_units,
            iodd_device=self.iodd_device,
            device_name=device_name,
            device_manufacturer=device_identity.vendor_name,
            variables=variables,
            process_data=process_data,
            texts=texts,
            datatypes=datatypes,
            errors=errors,
            units=units,
            user_interface=user_interface,
            images=self.images,
        )


@dataclass
class ResolvedIODD:
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
    :ivar user_interface: The resolved user interface with menus and role assignments.
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
    user_interface: ResolvedUserInterface

    images: list[IoddImage]

    def get_text(self, ref: TextRefT) -> str | None:
        """
        Get the text string for a text reference.

        :param ref: The text reference object containing the text_id.
        :returns: The resolved text string, or None if not found.
        """
        return self.texts.get(ref.text_id)
