"""
Resolver functions for IODD parsing.

This module contains helper functions that resolve references in IODD
data structures, merging information from standard definitions and
device-specific IODD files.
"""

from iodd_parser.generated.v1_1 import (
    AbstractVariableT,
    ArrayT,
    BooleanT,
    ButtonT,
    DataItemT,
    DatatypeT,
    ErrorTypeCollectionT,
    ErrorTypeT,
    Float32T,
    IntegerT,
    IoddstandardDefinitions,
    IoddstandardErrorTypeCollectionT,
    IoddstandardUnitDefinitions,
    IoddstandardVariableCollectionT,
    IoddstandardVariableT,
    Iodevice,
    LanguageT,
    MenuSetT,
    MenuT,
    OctetStringT,
    ProcessDataCollectionT,
    ProcessDataRefCollectionT,
    RecordT,
    StringT,
    TimeSpanT,
    TimeT,
    UimenuRefT,
    UintegerT,
    UirecordItemRefT,
    UivariableRefT,
    UserInterfaceT,
    VariableCollectionT,
)
from iodd_parser.types import (
    ResolvedArrayT,
    ResolvedBooleanT,
    ResolvedButton,
    ResolvedCondition,
    ResolvedDatatype,
    ResolvedError,
    ResolvedFloat32T,
    ResolvedIntegerT,
    ResolvedMenu,
    ResolvedMenuRef,
    ResolvedMenuSet,
    ResolvedOctetStringT,
    ResolvedProcessData,
    ResolvedProcessDataInfo,
    ResolvedProcessDataItem,
    ResolvedProcessDataRecordItemInfo,
    ResolvedProcessDataRef,
    ResolvedRecordItemRef,
    ResolvedRecordItemT,
    ResolvedRecordT,
    ResolvedSingleValue,
    ResolvedStringT,
    ResolvedTimeSpanT,
    ResolvedTimeT,
    ResolvedUIntegerT,
    ResolvedUnit,
    ResolvedUserInterface,
    ResolvedValueRange,
    ResolvedVariable,
    ResolvedVariableRef,
)


def _lang_id(lng: LanguageT) -> str:
    """
    Extract the language identifier from a LanguageT object.

    :param lng: The language object.
    :returns: The language identifier string.
    """
    if isinstance(lng.lang, str):
        return lng.lang
    return lng.lang.value


def resolve_texts(
    loaded_definitions: IoddstandardDefinitions,
    loaded_units: IoddstandardUnitDefinitions,
    device: Iodevice,
    lang: str | None,
    lang_texts: dict[str, dict[str, str]],
    device_lang_texts: dict[str, str],
) -> dict[str, str]:
    """
    Resolve text collections with language support.

    Texts are resolved in the following priority order (later sources override earlier ones):

    1. Primary language (English) from standard definitions
    2. Primary language from device IODD
    3. Primary language from standard unit definitions (English only)
    4. Pre-loaded language-specific standard definitions file (if available)
    5. Language sections within main standard definitions file
    6. Language sections within main device IODD file
    7. Device-specific language file (e.g., ``*-IODD1.1-de.xml``) - highest priority

    :param loaded_definitions: The loaded standard definitions.
    :param loaded_units: The loaded standard unit definitions.
    :param device: The parsed device IODD.
    :param lang: Optional language code (e.g., "de", "fr").
    :param lang_texts: Pre-loaded language-specific standard definitions texts.
    :param device_lang_texts: Texts from device-specific language file.
    :returns: Dictionary of resolved text strings keyed by text id.
    """
    # Always start with the primary language (English) as base
    texts: dict[str, str] = {t.id: t.value for t in loaded_definitions.external_text_collection.primary_language.text}
    texts.update({t.id: t.value for t in device.external_text_collection.primary_language.text})
    texts.update({t.id: t.value for t in loaded_units.external_text_collection.primary_language.text})

    # If a specific language is requested, overlay those texts on top
    if lang:
        # First, apply pre-loaded language-specific standard definitions texts
        if lang in lang_texts:
            texts.update(lang_texts[lang])

        # Also check for language sections within the main definitions file (fallback)
        lang_dfs = next(
            (x for x in loaded_definitions.external_text_collection.language if _lang_id(x) == lang),
            None,
        )
        if lang_dfs is not None:
            texts.update({t.id: t.value for t in lang_dfs.text})

        # Check for language sections within the main device IODD file
        lang_dev = next(
            (x for x in device.external_text_collection.language if _lang_id(x) == lang),
            None,
        )
        if lang_dev is not None:
            texts.update({t.id: t.value for t in lang_dev.text})

        # Finally, overlay device-specific language file texts (highest priority)
        if device_lang_texts:
            texts.update(device_lang_texts)

    return texts


def resolve_errors(
    std_error_collection: IoddstandardErrorTypeCollectionT,
    device_error_collection: ErrorTypeCollectionT | None,
    texts: dict[str, str],
) -> dict[tuple[int, int], ResolvedError]:
    """
    Resolve errors from standard definitions and device error collection.

    Combines referenced standard errors (code=128) with device-specific
    errors (code=129) into a unified dictionary.

    :param std_error_collection: Standard error types from definitions XML.
    :param device_error_collection: Device-specific error collection, may be None.
    :param texts: Dictionary of resolved text strings.
    :returns: Dictionary of resolved errors keyed by (code, additional_code) tuple.
    """
    errors: dict[tuple[int, int], ResolvedError] = {}

    if device_error_collection is None:
        return errors

    # Build lookup for standard errors by additional_code
    std_errors_lookup: dict[int, ErrorTypeT] = {err.additional_code: err for err in std_error_collection.error_type}

    # Add referenced standard errors (code=128)
    for ref in device_error_collection.std_error_type_ref:
        std_err = std_errors_lookup.get(ref.additional_code)
        if std_err is not None:
            key = (ref.code, ref.additional_code)
            errors[key] = ResolvedError(
                code=ref.code,
                additional_code=ref.additional_code,
                name=texts.get(std_err.name.text_id, std_err.name.text_id),
                description=(texts.get(std_err.description.text_id) if std_err.description else None),
            )

    # Add device-specific errors (code=129)
    for err in device_error_collection.error_type:
        key = (err.code, err.additional_code)
        errors[key] = ResolvedError(
            code=err.code,
            additional_code=err.additional_code,
            name=texts.get(err.name.text_id, err.name.text_id),
            description=(texts.get(err.description.text_id) if err.description else None),
        )

    return errors


def _get_datatype(
    item: AbstractVariableT | IoddstandardVariableT,
    datatypes: dict[str, DatatypeT],
) -> DatatypeT | None:
    """
    Get the datatype for a variable, resolving DatatypeRef if needed.

    :param item: The variable or standard variable object.
    :param datatypes: Dictionary of available datatypes keyed by id.
    :returns: The resolved DatatypeT, or None if not found.
    """
    if item.datatype is not None:
        return item.datatype
    if item.datatype_ref is not None:
        return datatypes.get(item.datatype_ref.datatype_id)
    return None


def _get_datatype_from_data_item(
    item: DataItemT,
    datatypes: dict[str, DatatypeT],
) -> DatatypeT | None:
    """
    Get the datatype for a data item, resolving DatatypeRef if needed.

    Used for ProcessDataItemT and similar data item types.

    :param item: The data item object (e.g., ProcessDataItemT).
    :param datatypes: Dictionary of available datatypes keyed by id.
    :returns: The resolved DatatypeT, or None if not found.
    """
    if item.datatype is not None:
        return item.datatype
    if item.datatype_ref is not None:
        return datatypes.get(item.datatype_ref.datatype_id)
    return None


def _resolve_single_values(
    single_values: list,
    texts: dict[str, str],
) -> list[ResolvedSingleValue]:
    """
    Resolve single values, converting TextRefT names to resolved strings.

    :param single_values: List of SingleValue objects (UIntegerValueT, etc.)
    :param texts: Dictionary of resolved text strings.
    :returns: List of ResolvedSingleValue objects.
    """
    result = []
    for sv in single_values:
        name = None
        if sv.name is not None and sv.name.text_id:
            name = texts.get(sv.name.text_id, sv.name.text_id)
        result.append(ResolvedSingleValue(value=sv.value, name=name))
    return result


def _resolve_value_ranges(
    value_ranges: list,
    texts: dict[str, str],
) -> list[ResolvedValueRange]:
    """
    Resolve value ranges, converting TextRefT names to resolved strings.

    :param value_ranges: List of ValueRange objects.
    :param texts: Dictionary of resolved text strings.
    :returns: List of ResolvedValueRange objects.
    """
    result = []
    for vr in value_ranges:
        name = None
        if vr.name is not None and vr.name.text_id:
            name = texts.get(vr.name.text_id, vr.name.text_id)
        result.append(
            ResolvedValueRange(
                lower_value=vr.lower_value,
                upper_value=vr.upper_value,
                name=name,
            )
        )
    return result


def _resolve_datatype(
    datatype: DatatypeT | None,
    texts: dict[str, str],
    datatypes: dict[str, DatatypeT],
) -> ResolvedDatatype:
    """
    Resolve a datatype to a ResolvedDatatype.

    Converts generated datatype objects to resolved types with all
    text references resolved to actual strings.

    :param datatype: The datatype to resolve, may be None.
    :param texts: Dictionary of resolved text strings.
    :param datatypes: Dictionary of available datatypes for resolving refs.
    :returns: A ResolvedDatatype or None.
    """
    if datatype is None:
        return None

    # Handle UIntegerT
    if isinstance(datatype, UintegerT):
        return ResolvedUIntegerT(
            bit_length=datatype.bit_length,
            single_values=_resolve_single_values(datatype.single_value, texts),
            value_ranges=_resolve_value_ranges(datatype.value_range, texts),
        )

    # Handle IntegerT
    if isinstance(datatype, IntegerT):
        return ResolvedIntegerT(
            bit_length=datatype.bit_length,
            single_values=_resolve_single_values(datatype.single_value, texts),
            value_ranges=_resolve_value_ranges(datatype.value_range, texts),
        )

    # Handle Float32T
    if isinstance(datatype, Float32T):
        return ResolvedFloat32T(
            single_values=_resolve_single_values(datatype.single_value, texts),
            value_ranges=_resolve_value_ranges(datatype.value_range, texts),
        )

    # Handle BooleanT
    if isinstance(datatype, BooleanT):
        return ResolvedBooleanT(
            single_values=_resolve_single_values(datatype.single_value, texts),
        )

    # Handle StringT
    if isinstance(datatype, StringT):
        return ResolvedStringT(
            fixed_length=datatype.fixed_length,
            encoding=datatype.encoding,
        )

    # Handle OctetStringT
    if isinstance(datatype, OctetStringT):
        return ResolvedOctetStringT(fixed_length=datatype.fixed_length)

    # Handle TimeT
    if isinstance(datatype, TimeT):
        return ResolvedTimeT()

    # Handle TimeSpanT
    if isinstance(datatype, TimeSpanT):
        return ResolvedTimeSpanT()

    # Handle RecordT
    if isinstance(datatype, RecordT):
        items = []
        for item in datatype.record_item:
            # Resolve the item's datatype
            item_datatype = None
            if item.simple_datatype is not None:
                item_datatype = _resolve_datatype(item.simple_datatype, texts, datatypes)
            elif item.datatype_ref is not None:
                ref_dt = datatypes.get(item.datatype_ref.datatype_id)
                item_datatype = _resolve_datatype(ref_dt, texts, datatypes)

            # Resolve name and description
            item_name = item.subindex  # fallback
            if item.name is not None and item.name.text_id:
                item_name = texts.get(item.name.text_id, item.name.text_id)

            item_desc = None
            if item.description is not None and item.description.text_id:
                item_desc = texts.get(item.description.text_id, item.description.text_id)

            items.append(
                ResolvedRecordItemT(
                    subindex=item.subindex,
                    bit_offset=item.bit_offset,
                    name=str(item_name),
                    description=item_desc,
                    datatype=item_datatype,
                )
            )

        return ResolvedRecordT(
            bit_length=datatype.bit_length,
            subindex_access_supported=datatype.subindex_access_supported,
            items=items,
        )

    # Handle ArrayT
    if isinstance(datatype, ArrayT):
        # Resolve element datatype
        element_datatype = None
        if datatype.simple_datatype is not None:
            element_datatype = _resolve_datatype(datatype.simple_datatype, texts, datatypes)
        elif datatype.datatype_ref is not None:
            ref_dt = datatypes.get(datatype.datatype_ref.datatype_id)
            element_datatype = _resolve_datatype(ref_dt, texts, datatypes)

        return ResolvedArrayT(
            count=datatype.count,
            subindex_access_supported=datatype.subindex_access_supported,
            element_datatype=element_datatype,
        )

    # Unknown datatype - return None
    return None


def resolve_variables(
    std_variable_collection: IoddstandardVariableCollectionT,
    device_variable_collection: VariableCollectionT,
    texts: dict[str, str],
    datatypes: dict[str, DatatypeT],
) -> dict[str, ResolvedVariable]:
    """
    Resolve variables from standard definitions and device variable collection.

    Variables come from three sources:

    - **StdVariableRef**: references to standard variables from
      IODD-StandardDefinitions1.1.xml
    - **DirectParameterOverlay**: device-specific data within DirectParameter page
    - **Variable**: vendor-specific variables with a device-specific index

    :param std_variable_collection: Standard variables from definitions XML.
    :param device_variable_collection: Device variable collection from IODD.
    :param texts: Dictionary of resolved text strings.
    :param datatypes: Dictionary of available datatypes.
    :returns: Dictionary of resolved variables keyed by variable id.
    """
    variables: dict[str, ResolvedVariable] = {}

    # Build lookup for standard variables by id
    std_vars_lookup: dict[str, IoddstandardVariableT] = {var.id: var for var in std_variable_collection.variable}

    # 1. Add referenced standard variables (StdVariableRef)
    for ref in device_variable_collection.std_variable_ref:
        std_var = std_vars_lookup.get(ref.id)
        if std_var is None:
            continue

        raw_datatype = _get_datatype(std_var, datatypes)
        resolved_datatype = _resolve_datatype(raw_datatype, texts, datatypes)

        variables[ref.id] = ResolvedVariable(
            id=ref.id,
            index=std_var.index,
            datatype=resolved_datatype,
            name=texts.get(std_var.name.text_id, std_var.name.text_id),
            description=(texts.get(std_var.description.text_id) if std_var.description else None),
            access_rights=std_var.access_rights,
            dynamic=std_var.dynamic,
            modifies_other_variables=std_var.modifies_other_variables,
            # excludedFromDataStorage can be overridden by StdVariableRef
            excluded_from_data_storage=(ref.excluded_from_data_storage or std_var.excluded_from_data_storage),
            default_value=ref.default_value,
            fixed_length_restriction=ref.fixed_length_restriction,
            record_item_info=std_var.record_item_info,
        )

    # 2. Add DirectParameterOverlay if present (index=1 for V_DirectParameters_2)
    if device_variable_collection.direct_parameter_overlay is not None:
        overlay = device_variable_collection.direct_parameter_overlay
        raw_datatype = _get_datatype(overlay, datatypes)
        resolved_datatype = _resolve_datatype(raw_datatype, texts, datatypes)

        variables[overlay.id] = ResolvedVariable(
            id=overlay.id,
            index=1,  # DirectParameterOverlay maps to index 1 (V_DirectParameters_2)
            datatype=resolved_datatype,
            name=texts.get(overlay.name.text_id, overlay.name.text_id),
            description=(texts.get(overlay.description.text_id) if overlay.description else None),
            access_rights=overlay.access_rights,
            dynamic=overlay.dynamic,
            modifies_other_variables=overlay.modifies_other_variables,
            excluded_from_data_storage=overlay.excluded_from_data_storage,
            record_item_info=overlay.record_item_info,
        )

    # 3. Add vendor-specific variables (Variable)
    for var in device_variable_collection.variable:
        raw_datatype = _get_datatype(var, datatypes)
        resolved_datatype = _resolve_datatype(raw_datatype, texts, datatypes)

        variables[var.id] = ResolvedVariable(
            id=var.id,
            index=var.index,
            datatype=resolved_datatype,
            name=texts.get(var.name.text_id, var.name.text_id),
            description=(texts.get(var.description.text_id) if var.description else None),
            access_rights=var.access_rights,
            dynamic=var.dynamic,
            modifies_other_variables=var.modifies_other_variables,
            excluded_from_data_storage=var.excluded_from_data_storage,
            default_value=var.default_value,
            record_item_info=var.record_item_info,
        )

    return variables


def resolve_units(
    unit_definitions: IoddstandardUnitDefinitions,
    texts: dict[str, str],
) -> dict[int, ResolvedUnit]:
    """
    Resolve units from standard unit definitions.

    :param unit_definitions: The parsed standard unit definitions XML.
    :param texts: Dictionary of resolved text strings.
    :returns: Dictionary of resolved units keyed by unit code.
    """
    units: dict[int, ResolvedUnit] = {}
    for unit in unit_definitions.unit_collection.unit:
        units[unit.code] = ResolvedUnit(
            code=unit.code,
            abbreviation=unit.abbr,
            name=texts.get(unit.text_id, unit.text_id),
        )
    return units


def resolve_process_data(
    process_data_collection: ProcessDataCollectionT | None,
    texts: dict[str, str],
    datatypes: dict[str, DatatypeT],
) -> dict[str, ResolvedProcessData]:
    """
    Resolve process data from the ProcessDataCollection.

    Process data defines the structure of cyclic data exchanged between
    master and device. Multiple ProcessData elements can exist with
    Condition elements for switching between configurations.

    :param process_data_collection: The process data collection, may be None.
    :param texts: Dictionary of resolved text strings.
    :param datatypes: Dictionary of available datatypes.
    :returns: Dictionary of resolved process data keyed by ProcessData id.
    """
    if process_data_collection is None:
        return {}

    result: dict[str, ResolvedProcessData] = {}

    for pd in process_data_collection.process_data:
        # Extract condition information if present
        condition_var_id = None
        condition_subindex = None
        condition_value = None

        if pd.condition is not None:
            condition_var_id = pd.condition.variable_id
            condition_subindex = pd.condition.subindex
            condition_value = pd.condition.value

        # Resolve ProcessDataIn
        pd_in = None
        if pd.process_data_in is not None:
            pdi = pd.process_data_in
            raw_dt = _get_datatype_from_data_item(pdi, datatypes)
            pd_in = ResolvedProcessDataItem(
                id=pdi.id,
                bit_length=pdi.bit_length,
                name=texts.get(pdi.name.text_id, pdi.name.text_id),
                datatype=_resolve_datatype(raw_dt, texts, datatypes),
            )

        # Resolve ProcessDataOut
        pd_out = None
        if pd.process_data_out is not None:
            pdo = pd.process_data_out
            raw_dt = _get_datatype_from_data_item(pdo, datatypes)
            pd_out = ResolvedProcessDataItem(
                id=pdo.id,
                bit_length=pdo.bit_length,
                name=texts.get(pdo.name.text_id, pdo.name.text_id),
                datatype=_resolve_datatype(raw_dt, texts, datatypes),
            )

        result[pd.id] = ResolvedProcessData(
            id=pd.id,
            process_data_in=pd_in,
            process_data_out=pd_out,
            condition_variable_id=condition_var_id,
            condition_subindex=condition_subindex,
            condition_value=condition_value,
        )

    return result


def _resolve_button(button: ButtonT | None, texts: dict[str, str]) -> ResolvedButton | None:
    """
    Resolve a Button element to a ResolvedButton.

    :param button: The button element, may be None.
    :param texts: Dictionary of resolved text strings.
    :returns: Resolved button or None if button is None.
    """
    if button is None:
        return None

    return ResolvedButton(
        button_value=button.button_value,
        description=(texts.get(button.description.text_id) if button.description is not None else None),
        action_started_message=(
            texts.get(button.action_started_message.text_id) if button.action_started_message is not None else None
        ),
    )


def _resolve_variable_ref(
    ref: UivariableRefT,
    texts: dict[str, str],
) -> ResolvedVariableRef:
    """
    Resolve a VariableRef element to a ResolvedVariableRef.

    :param ref: The variable reference element.
    :param texts: Dictionary of resolved text strings.
    :returns: Resolved variable reference.
    """
    return ResolvedVariableRef(
        variable_id=ref.variable_id,
        gradient=ref.gradient,
        offset=ref.offset,
        unit_code=ref.unit_code,
        display_format=ref.display_format,
        access_right_restriction=ref.access_right_restriction,
        button=_resolve_button(ref.button, texts),
    )


def _resolve_record_item_ref(
    ref: UirecordItemRefT,
    texts: dict[str, str],
) -> ResolvedRecordItemRef:
    """
    Resolve a RecordItemRef element to a ResolvedRecordItemRef.

    :param ref: The record item reference element.
    :param texts: Dictionary of resolved text strings.
    :returns: Resolved record item reference.
    """
    return ResolvedRecordItemRef(
        variable_id=ref.variable_id,
        subindex=ref.subindex,
        gradient=ref.gradient,
        offset=ref.offset,
        unit_code=ref.unit_code,
        display_format=ref.display_format,
        access_right_restriction=ref.access_right_restriction,
        button=_resolve_button(ref.button, texts),
    )


def _resolve_menu_ref(ref: UimenuRefT) -> ResolvedMenuRef:
    """
    Resolve a MenuRef element to a ResolvedMenuRef.

    :param ref: The menu reference element.
    :returns: Resolved menu reference.
    """
    condition = None
    if ref.condition is not None:
        condition = ResolvedCondition(
            variable_id=ref.condition.variable_id,
            subindex=ref.condition.subindex,
            value=ref.condition.value,
        )

    return ResolvedMenuRef(
        menu_id=ref.menu_id,
        condition=condition,
    )


def _resolve_menu(menu: MenuT, texts: dict[str, str]) -> ResolvedMenu:
    """
    Resolve a Menu element to a ResolvedMenu.

    :param menu: The menu element.
    :param texts: Dictionary of resolved text strings.
    :returns: Resolved menu.
    """
    name = None
    if menu.name is not None:
        name = texts.get(menu.name.text_id)

    return ResolvedMenu(
        id=menu.id,
        name=name,
        variable_refs=[_resolve_variable_ref(ref, texts) for ref in menu.variable_ref],
        record_item_refs=[_resolve_record_item_ref(ref, texts) for ref in menu.record_item_ref],
        menu_refs=[_resolve_menu_ref(ref) for ref in menu.menu_ref],
    )


def _resolve_menu_set(menu_set: MenuSetT) -> ResolvedMenuSet:
    """
    Resolve a MenuSet element to a ResolvedMenuSet.

    :param menu_set: The menu set element.
    :returns: Resolved menu set.
    """
    return ResolvedMenuSet(
        identification_menu_id=menu_set.identification_menu.menu_id,
        parameter_menu_id=(menu_set.parameter_menu.menu_id if menu_set.parameter_menu else None),
        observation_menu_id=(menu_set.observation_menu.menu_id if menu_set.observation_menu else None),
        diagnosis_menu_id=(menu_set.diagnosis_menu.menu_id if menu_set.diagnosis_menu else None),
    )


def _resolve_process_data_refs(
    collection: ProcessDataRefCollectionT | None,
) -> list[ResolvedProcessDataRef]:
    """
    Resolve ProcessDataRefCollection to a list of ResolvedProcessDataRef.

    :param collection: The process data ref collection, may be None.
    :returns: List of resolved process data references.
    """
    if collection is None:
        return []

    result: list[ResolvedProcessDataRef] = []

    for ref in collection.process_data_ref:
        # Resolve ProcessDataInfo if present (for non-record types)
        pd_info = None
        if ref.process_data_info is not None:
            info = ref.process_data_info
            pd_info = ResolvedProcessDataInfo(
                gradient=info.gradient,
                offset=info.offset,
                unit_code=info.unit_code,
                display_format=info.display_format,
            )

        # Resolve ProcessDataRecordItemInfo list (for record types)
        record_item_infos: list[ResolvedProcessDataRecordItemInfo] = []
        for item_info in ref.process_data_record_item_info:
            record_item_infos.append(
                ResolvedProcessDataRecordItemInfo(
                    subindex=item_info.subindex,
                    gradient=item_info.gradient,
                    offset=item_info.offset,
                    unit_code=item_info.unit_code,
                    display_format=item_info.display_format,
                )
            )

        result.append(
            ResolvedProcessDataRef(
                process_data_id=ref.process_data_id,
                process_data_info=pd_info,
                record_item_infos=record_item_infos,
            )
        )

    return result


def resolve_user_interface(
    user_interface: UserInterfaceT,
    texts: dict[str, str],
) -> ResolvedUserInterface:
    """
    Resolve the UserInterface element to a ResolvedUserInterface.

    The UserInterface contains:
    - ProcessDataRefCollection (optional): Display info for process data
    - MenuCollection: All menu definitions
    - Three role-based MenuSets: Observer, Maintenance, Specialist

    Each role has fixed top-level menus (Identification, Parameter,
    Observation, Diagnosis) that reference menus from the MenuCollection.

    :param user_interface: The user interface element from DeviceFunction.
    :param texts: Dictionary of resolved text strings.
    :returns: Resolved user interface with all menus and role assignments.
    """
    # Resolve all menus from MenuCollection
    menus: dict[str, ResolvedMenu] = {}
    for menu in user_interface.menu_collection.menu:
        menus[menu.id] = _resolve_menu(menu, texts)

    # Resolve the three role menu sets
    observer_menu_set = _resolve_menu_set(user_interface.observer_role_menu_set)
    maintenance_menu_set = _resolve_menu_set(user_interface.maintenance_role_menu_set)
    specialist_menu_set = _resolve_menu_set(user_interface.specialist_role_menu_set)

    # Resolve process data references
    process_data_refs = _resolve_process_data_refs(user_interface.process_data_ref_collection)

    return ResolvedUserInterface(
        menus=menus,
        observer_role_menu_set=observer_menu_set,
        maintenance_role_menu_set=maintenance_menu_set,
        specialist_role_menu_set=specialist_menu_set,
        process_data_refs=process_data_refs,
    )
