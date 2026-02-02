"""
Resolver functions for IODD parsing.

This module contains helper functions that resolve references in IODD
data structures, merging information from standard definitions and
device-specific IODD files.
"""

from iodd_parser.generated.v1_1 import (
    AbstractVariableT,
    DataItemT,
    DatatypeT,
    ErrorTypeCollectionT,
    ErrorTypeT,
    IoddstandardErrorTypeCollectionT,
    IoddstandardUnitDefinitions,
    IoddstandardVariableCollectionT,
    IoddstandardVariableT,
    ProcessDataCollectionT,
    VariableCollectionT,
)
from iodd_parser.types import (
    ResolvedError,
    ResolvedProcessData,
    ResolvedProcessDataItem,
    ResolvedUnit,
    ResolvedVariable,
)



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
    std_errors_lookup: dict[int, ErrorTypeT] = {
        err.additional_code: err for err in std_error_collection.error_type
    }

    # Add referenced standard errors (code=128)
    for ref in device_error_collection.std_error_type_ref:
        std_err = std_errors_lookup.get(ref.additional_code)
        if std_err is not None:
            key = (ref.code, ref.additional_code)
            errors[key] = ResolvedError(
                code=ref.code,
                additional_code=ref.additional_code,
                name=texts.get(std_err.name.text_id, std_err.name.text_id),
                description=(
                    texts.get(std_err.description.text_id)
                    if std_err.description
                    else None
                ),
            )

    # Add device-specific errors (code=129)
    for err in device_error_collection.error_type:
        key = (err.code, err.additional_code)
        errors[key] = ResolvedError(
            code=err.code,
            additional_code=err.additional_code,
            name=texts.get(err.name.text_id, err.name.text_id),
            description=(
                texts.get(err.description.text_id) if err.description else None
            ),
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
    std_vars_lookup: dict[str, IoddstandardVariableT] = {
        var.id: var for var in std_variable_collection.variable
    }

    # 1. Add referenced standard variables (StdVariableRef)
    for ref in device_variable_collection.std_variable_ref:
        std_var = std_vars_lookup.get(ref.id)
        if std_var is None:
            continue

        variables[ref.id] = ResolvedVariable(
            id=ref.id,
            index=std_var.index,
            datatype=_get_datatype(std_var, datatypes),
            name=texts.get(std_var.name.text_id, std_var.name.text_id),
            description=(
                texts.get(std_var.description.text_id)
                if std_var.description
                else None
            ),
            access_rights=std_var.access_rights,
            dynamic=std_var.dynamic,
            modifies_other_variables=std_var.modifies_other_variables,
            # excludedFromDataStorage can be overridden by StdVariableRef
            excluded_from_data_storage=(
                ref.excluded_from_data_storage or std_var.excluded_from_data_storage
            ),
            default_value=ref.default_value,
            fixed_length_restriction=ref.fixed_length_restriction,
            record_item_info=std_var.record_item_info,
        )

    # 2. Add DirectParameterOverlay if present (index=1 for V_DirectParameters_2)
    if device_variable_collection.direct_parameter_overlay is not None:
        overlay = device_variable_collection.direct_parameter_overlay
        variables[overlay.id] = ResolvedVariable(
            id=overlay.id,
            index=1,  # DirectParameterOverlay maps to index 1 (V_DirectParameters_2)
            datatype=_get_datatype(overlay, datatypes),
            name=texts.get(overlay.name.text_id, overlay.name.text_id),
            description=(
                texts.get(overlay.description.text_id)
                if overlay.description
                else None
            ),
            access_rights=overlay.access_rights,
            dynamic=overlay.dynamic,
            modifies_other_variables=overlay.modifies_other_variables,
            excluded_from_data_storage=overlay.excluded_from_data_storage,
            record_item_info=overlay.record_item_info,
        )

    # 3. Add vendor-specific variables (Variable)
    for var in device_variable_collection.variable:
        variables[var.id] = ResolvedVariable(
            id=var.id,
            index=var.index,
            datatype=_get_datatype(var, datatypes),
            name=texts.get(var.name.text_id, var.name.text_id),
            description=(
                texts.get(var.description.text_id) if var.description else None
            ),
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
            pd_in = ResolvedProcessDataItem(
                id=pdi.id,
                bit_length=pdi.bit_length,
                name=texts.get(pdi.name.text_id, pdi.name.text_id),
                datatype=_get_datatype_from_data_item(pdi, datatypes),
            )

        # Resolve ProcessDataOut
        pd_out = None
        if pd.process_data_out is not None:
            pdo = pd.process_data_out
            pd_out = ResolvedProcessDataItem(
                id=pdo.id,
                bit_length=pdo.bit_length,
                name=texts.get(pdo.name.text_id, pdo.name.text_id),
                datatype=_get_datatype_from_data_item(pdo, datatypes),
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
