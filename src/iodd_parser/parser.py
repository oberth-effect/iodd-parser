import io
import zipfile
from dataclasses import dataclass, field
from importlib.resources import files
from importlib.resources.abc import Traversable
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser

from iodd_parser.generated.v1_1 import (
    AbstractVariableT,
    AccessRightsT,
    DatatypeT,
    ErrorTypeCollectionT,
    ErrorTypeT,
    IoddstandardDefinitions,
    IoddstandardErrorTypeCollectionT,
    IoddstandardUnitDefinitions,
    IoddstandardVariableCollectionT,
    IoddstandardVariableT,
    Iodevice,
    LanguageT,
    RecordItemInfoT,
    TextDefinitionT,
    TextRefT,
    VariableCollectionT,
)

STANDARD_DEFINITIONS_PACKAGE = "iodd_parser.standard_definitions"
STANDARD_DEFINITIONS_VERSION = "v1_1"

IODD_IMAGE_FORMATS = {
    ".png",
}


@dataclass
class IoddImage:
    filename: str
    data: bytes


@dataclass
class ResolvedVariable:
    """A resolved variable with all references resolved.

    Variables can come from three sources:
    - StdVariableRef: references to standard variables from IODD-StandardDefinitions1.1.xml
    - DirectParameterOverlay: device-specific data within DirectParameter page
    - Variable: vendor-specific variables with a device-specific index
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
    code: int
    additional_code: int
    name: str
    description: None | str


@dataclass
class ResolvedUnit:
    """A resolved unit with its code, abbreviation, and name.

    The units are defined in IODD-StandardUnitDefinitions1.1.xml.
    - code: the unit code (e.g. 1001 for degrees Celsius)
    - abbreviation: the short form (e.g. "°C")
    - name: the full name (e.g. "degree Celsius")
    """

    code: int
    abbreviation: str
    name: str


@dataclass
class ParsedIODD:
    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice

    device_name: str
    device_manufacturer: str
    variables: list[ResolvedVariable]
    texts: dict[str, str]
    datatypes: dict[str, DatatypeT]
    errors: dict[tuple[int, int], ResolvedError]
    units: dict[int, ResolvedUnit]

    images: list[IoddImage]

    def get_text(self, ref: TextRefT) -> str | None:
        return self.texts.get(ref.text_id)


def _merge_texts(definitions: list[TextDefinitionT], device: list[TextDefinitionT]) -> dict[str, str]:
    text_dict = {d.id: d.value for d in definitions}
    text_dict.update({d.id: d.value for d in device})
    return text_dict


def _lang_id(lng: LanguageT) -> str:
    if isinstance(lng.lang, str):
        return lng.lang
    return lng.lang.value


def _resolve_standard_definition_source(value: str | Path) -> Path | Traversable:
    if isinstance(value, Path):
        return value

    if isinstance(value, str):
        resource_dir = files(STANDARD_DEFINITIONS_PACKAGE).joinpath(STANDARD_DEFINITIONS_VERSION)
        file_path = Path(value)
        if len(file_path.parts) == 1:
            candidate = resource_dir.joinpath(file_path.name)
            if candidate.is_file():
                return candidate
        return file_path

    raise TypeError(f"Unsupported standard definition type: {type(value)!r}")


def _resolve_errors(
    std_error_collection: IoddstandardErrorTypeCollectionT,
    device_error_collection: ErrorTypeCollectionT | None,
    texts: dict[str, str],
) -> dict[tuple[int, int], ResolvedError]:
    """Resolve errors from standard definitions and device error collection.

    Returns a dict keyed by (code, additional_code) tuple.
    - Standard errors have code=128
    - Device-specific errors have code=129
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
                description=texts.get(std_err.description.text_id) if std_err.description else None,
            )

    # Add device-specific errors (code=129)
    for err in device_error_collection.error_type:
        key = (err.code, err.additional_code)
        errors[key] = ResolvedError(
            code=err.code,
            additional_code=err.additional_code,
            name=texts.get(err.name.text_id, err.name.text_id),
            description=texts.get(err.description.text_id) if err.description else None,
        )

    return errors


def _get_datatype(
    item: AbstractVariableT | IoddstandardVariableT,
    datatypes: dict[str, DatatypeT],
) -> DatatypeT | None:
    """Get the datatype for a variable, resolving DatatypeRef if needed."""
    if item.datatype is not None:
        return item.datatype
    if item.datatype_ref is not None:
        return datatypes.get(item.datatype_ref.datatype_id)
    return None


def _resolve_variables(
    std_variable_collection: IoddstandardVariableCollectionT,
    device_variable_collection: VariableCollectionT,
    texts: dict[str, str],
    datatypes: dict[str, DatatypeT],
) -> list[ResolvedVariable]:
    """Resolve variables from standard definitions and device variable collection.

    Variables come from three sources:
    - StdVariableRef: references to standard variables from IODD-StandardDefinitions1.1.xml
    - DirectParameterOverlay: device-specific data within DirectParameter page
    - Variable: vendor-specific variables with a device-specific index
    """
    variables: list[ResolvedVariable] = []

    # Build lookup for standard variables by id
    std_vars_lookup: dict[str, IoddstandardVariableT] = {var.id: var for var in std_variable_collection.variable}

    # 1. Add referenced standard variables (StdVariableRef)
    for ref in device_variable_collection.std_variable_ref:
        std_var = std_vars_lookup.get(ref.id)
        if std_var is None:
            continue

        variables.append(
            ResolvedVariable(
                id=ref.id,
                index=std_var.index,
                datatype=_get_datatype(std_var, datatypes),
                name=texts.get(std_var.name.text_id, std_var.name.text_id),
                description=texts.get(std_var.description.text_id) if std_var.description else None,
                access_rights=std_var.access_rights,
                dynamic=std_var.dynamic,
                modifies_other_variables=std_var.modifies_other_variables,
                # excludedFromDataStorage can be overridden by StdVariableRef
                excluded_from_data_storage=ref.excluded_from_data_storage or std_var.excluded_from_data_storage,
                default_value=ref.default_value,
                fixed_length_restriction=ref.fixed_length_restriction,
                record_item_info=std_var.record_item_info,
            )
        )

    # 2. Add DirectParameterOverlay if present (index=1 for V_DirectParameters_2)
    if device_variable_collection.direct_parameter_overlay is not None:
        overlay = device_variable_collection.direct_parameter_overlay
        variables.append(
            ResolvedVariable(
                id=overlay.id,
                index=1,  # DirectParameterOverlay maps to index 1 (V_DirectParameters_2)
                datatype=_get_datatype(overlay, datatypes),
                name=texts.get(overlay.name.text_id, overlay.name.text_id),
                description=texts.get(overlay.description.text_id) if overlay.description else None,
                access_rights=overlay.access_rights,
                dynamic=overlay.dynamic,
                modifies_other_variables=overlay.modifies_other_variables,
                excluded_from_data_storage=overlay.excluded_from_data_storage,
                record_item_info=overlay.record_item_info,
            )
        )

    # 3. Add vendor-specific variables (Variable)
    for var in device_variable_collection.variable:
        variables.append(
            ResolvedVariable(
                id=var.id,
                index=var.index,
                datatype=_get_datatype(var, datatypes),
                name=texts.get(var.name.text_id, var.name.text_id),
                description=texts.get(var.description.text_id) if var.description else None,
                access_rights=var.access_rights,
                dynamic=var.dynamic,
                modifies_other_variables=var.modifies_other_variables,
                excluded_from_data_storage=var.excluded_from_data_storage,
                default_value=var.default_value,
                record_item_info=var.record_item_info,
            )
        )

    return variables


def _resolve_units(
    unit_definitions: IoddstandardUnitDefinitions,
    texts: dict[str, str],
) -> dict[int, ResolvedUnit]:
    """Resolve units from standard unit definitions.

    Returns a dict keyed by unit code.
    """
    units: dict[int, ResolvedUnit] = {}
    for unit in unit_definitions.unit_collection.unit:
        units[unit.code] = ResolvedUnit(
            code=unit.code,
            abbreviation=unit.abbr,
            name=texts.get(unit.text_id, unit.text_id),
        )

    return units


class IODDParser:
    load_images: bool

    _loaded_definitions: IoddstandardDefinitions
    _loaded_units: IoddstandardUnitDefinitions

    def __init__(
        self,
        standard_definitions: str | Path = "IODD-StandardDefinitions1.1.xml",
        standard_unit_definitions: str | Path = "IODD-StandardUnitDefinitions1.1.xml",
        load_images: bool = False,
    ):
        self.load_images = load_images

        parser = XmlParser()

        definitions_source = _resolve_standard_definition_source(standard_definitions)
        units_source = _resolve_standard_definition_source(standard_unit_definitions)

        self._loaded_definitions = parser.parse(definitions_source, IoddstandardDefinitions)
        self._loaded_units = parser.parse(units_source, IoddstandardUnitDefinitions)

    def parse(self, zip_path: str | Path, lang=None) -> ParsedIODD:
        zip_pth = Path(zip_path)
        if not zip_pth.is_file():
            raise FileNotFoundError(f"IODD zip not found: {zip_pth.resolve()}")

        xml_suffix = f"-IODD1.1-{lang}.xml" if lang else "-IODD1.1.xml"

        with zipfile.ZipFile(zip_pth, "r") as archive:
            xml_suffix_lower = xml_suffix.lower()
            xml_candidates = [
                name
                for name in archive.namelist()
                if not name.endswith("/") and name.lower().endswith(xml_suffix_lower)
            ]

            if not xml_candidates:
                raise FileNotFoundError(f"Expected IODD XML with suffix '{xml_suffix}' not found in {zip_pth.name}")
            if len(xml_candidates) > 1:
                raise ValueError(f"Multiple IODD XML files with suffix '{xml_suffix}' found: {xml_candidates}")

            xml_data = archive.read(xml_candidates[0])
            device = XmlParser().parse(io.BytesIO(xml_data), Iodevice)

            images: list[IoddImage] = []
            if self.load_images:
                for name in archive.namelist():
                    if name.endswith("/"):
                        continue
                    if Path(name).suffix.lower() in IODD_IMAGE_FORMATS:
                        images.append(IoddImage(filename=name, data=archive.read(name)))

        text_col_dfs = self._loaded_definitions.external_text_collection.primary_language
        text_col_dev = device.external_text_collection.primary_language

        if lang:
            text_col_dfs = next(
                (x for x in self._loaded_definitions.external_text_collection.language if _lang_id(x) == lang),
                text_col_dfs,
            )
            text_col_dev = next(
                (x for x in device.external_text_collection.language if _lang_id(x) == lang),
                text_col_dev,
            )

        # Get unit texts with language support
        text_col_units = self._loaded_units.external_text_collection.primary_language
        if lang:
            text_col_units = next(
                (x for x in self._loaded_units.external_text_collection.language if _lang_id(x) == lang),
                text_col_units,
            )

        texts = _merge_texts(text_col_dfs.text, text_col_dev.text)
        texts.update({t.id: t.value for t in text_col_units.text})

        # Build datatypes lookup from both standard definitions and device
        datatypes: dict[str, DatatypeT] = {}
        if self._loaded_definitions.datatype_collection is not None:
            for dt in self._loaded_definitions.datatype_collection.datatype:
                if dt.id is not None:
                    datatypes[dt.id] = dt
        if device.profile_body.device_function.datatype_collection is not None:
            for dt in device.profile_body.device_function.datatype_collection.datatype:
                if dt.id is not None:
                    datatypes[dt.id] = dt

        errors = _resolve_errors(
            self._loaded_definitions.error_type_collection,
            device.profile_body.device_function.error_type_collection,
            texts,
        )

        units = _resolve_units(self._loaded_units, texts)

        variables = _resolve_variables(
            self._loaded_definitions.variable_collection,
            device.profile_body.device_function.variable_collection,
            texts,
            datatypes,
        )

        device_identity = device.profile_body.device_identity
        device_name = texts.get(device_identity.device_name.text_id, device_identity.device_name.text_id)

        return ParsedIODD(
            iodd_definitions=self._loaded_definitions,
            iodd_units=self._loaded_units,
            iodd_device=device,
            device_name=device_name,
            device_manufacturer=device_identity.vendor_name,
            variables=variables,
            texts=texts,
            datatypes=datatypes,
            errors=errors,
            units=units,
            images=images,
        )

    @property
    def standard_definitions(self):
        return self._loaded_definitions

    @property
    def standard_definition_units(self):
        return self._loaded_units
