# IODD Parser

A simple Python package for parsing [IO-Link Device Description (IODD)](https://ioddfinder.io-link.com/) v1.1 files.

Built on top of [`xsdata`](https://github.com/tefra/xsdata)-generated parsers from the official
[IO-Link Specification](https://io-link.com/downloads) XSD schema files (snippets schema excluded), this package provides
a convenient API that resolves references (texts, datatypes, variables, errors, units)
into unified data structures.

## Installation

```bash
pip install iodd-parser
```

## Usage

### Basic Usage

```python
from iodd_parser import IODDParser

parser = IODDParser()

# Parse and resolve in one step
result = parser.parse_and_resolve("path/to/device-IODD1.1.zip")

print(result.device_name)
print(result.device_manufacturer)

# Access resolved variables by ID
for var_id, var in result.variables.items():
    print(f"{var_id}: {var.name} (index={var.index})")

# Access resolved process data
for pd_id, pd in result.process_data.items():
    if pd.process_data_in:
        print(f"Input: {pd.process_data_in.name} ({pd.process_data_in.bit_length} bits)")

# Access resolved errors
for (code, additional_code), error in result.errors.items():
    print(f"Error {code}/{additional_code}: {error.name}")

# Access resolved units
for unit_code, unit in result.units.items():
    print(f"Unit {unit_code}: {unit.name} ({unit.abbreviation})")
```

### Two-Step Parse and Resolve

For more control, you can separate the parse and resolve steps:

```python
from iodd_parser import IODDParser

parser = IODDParser()

# Step 1: Parse the IODD file (discovers all available languages)
parsed = parser.parse("path/to/device-IODD1.1.zip")

# Check available languages
print(f"Available languages: {parsed.available_languages}")

# Step 2: Resolve with a specific language
result = parsed.resolve(lang="de")
```

### Language Support

The parser supports multiple languages for text resolution. Language-specific standard
definition files are auto-discovered and pre-loaded at parser initialisation, and device-specific
language files are discovered automatically from the IODD ZIP archive during parsing.

```python
from iodd_parser import IODDParser

parser = IODDParser()

# Parse the IODD file (all language files are discovered)
parsed = parser.parse("path/to/device-IODD1.1.zip")

# Check what languages are available
print(f"Available: {parsed.available_languages}")  # e.g., {'de', 'fr', 'es', ...}

# Resolve with German texts
result = parsed.resolve(lang="de")

# Variable names are now in German
print(result.variables["V_VendorName"].name)  # "Herstellername"

# Or use the convenience method
result = parser.parse_and_resolve("path/to/device-IODD1.1.zip", lang="de")
```

### Custom Standard Definitions Folder

You can load standard definitions from a custom folder instead of the bundled files:

```python
from iodd_parser import IODDParser

parser = IODDParser(standard_definitions_folder="/path/to/definitions")
```

### Loading Images

```python
from iodd_parser import IODDParser

parser = IODDParser(load_images=True)
result = parser.parse("path/to/device-IODD1.1.zip")

for image in result.images:
    print(f"Image: {image.filename} ({len(image.data)} bytes)")
```

## Result Structure

### ParsedIODD

The `parse()` method returns a `ParsedIODD` object containing the raw parsed data:

```python
@dataclass
class ParsedIODD:
    # Raw parsed objects (as per IODD schema)
    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice

    # Language texts from standard definitions and device
    standard_lang_texts: dict[str, dict[str, str]]  # lang -> text_id -> text
    device_lang_texts: dict[str, dict[str, str]]    # lang -> text_id -> text

    # Extracted images (if load_images=True)
    images: list[IoddImage]

    # Properties and methods
    available_languages: set[str]  # All discovered language codes
    def resolve(self, lang: str | None = None) -> ResolvedIODD: ...
```

### ResolvedIODD

The `resolve()` method (or `parse_and_resolve()`) returns a `ResolvedIODD` object:

```python
@dataclass
class ResolvedIODD:
    # Raw parsed objects (as per IODD schema)
    iodd_definitions: IoddstandardDefinitions
    iodd_units: IoddstandardUnitDefinitions
    iodd_device: Iodevice

    # Resolved device information
    device_name: str
    device_manufacturer: str

    # Resolved collections (with all references resolved)
    variables: dict[str, ResolvedVariable]      # Keyed by variable ID
    process_data: dict[str, ResolvedProcessData]  # Keyed by process data ID
    texts: dict[str, str]                       # Keyed by text ID
    datatypes: dict[str, DatatypeT]             # Keyed by datatype ID (raw types)
    errors: dict[tuple[int, int], ResolvedError]  # Keyed by (code, additional_code)
    units: dict[int, ResolvedUnit]              # Keyed by unit code
    user_interface: ResolvedUserInterface       # Menus and role assignments

    # Extracted images (if load_images=True)
    images: list[IoddImage]
```

### Resolved Types

#### Variables and Data

- **`ResolvedVariable`**: Variables from StdVariableRef, DirectParameterOverlay, or vendor-specific Variable elements
- **`ResolvedError`**: Error types (code=128 for standard, code=129 for vendor-specific)
- **`ResolvedUnit`**: Unit definitions with code, abbreviation, and name
- **`ResolvedProcessData`**: Process data configuration with optional condition for switching
- **`ResolvedProcessDataItem`**: Individual process data input/output description

#### Resolved Datatypes

Variables and process data items have a `datatype` field containing one of the following resolved types (instead of raw generated types):

- **`ResolvedUIntegerT`**: Unsigned integer with `bit_length`, `single_values`, and `value_ranges`
- **`ResolvedIntegerT`**: Signed integer with `bit_length`, `single_values`, and `value_ranges`
- **`ResolvedFloat32T`**: 32-bit float with `single_values` and `value_ranges`
- **`ResolvedBooleanT`**: Boolean with `single_values` (for true/false labels)
- **`ResolvedStringT`**: String with `fixed_length` and `encoding`
- **`ResolvedOctetStringT`**: Byte array with `fixed_length`
- **`ResolvedTimeT`**: Absolute timestamp
- **`ResolvedTimeSpanT`**: Duration/time span
- **`ResolvedRecordT`**: Record/struct with `bit_length`, `subindex_access_supported`, and `items`
- **`ResolvedArrayT`**: Array with `count`, `subindex_access_supported`, and `element_datatype`

Single values and value ranges have their text references resolved:

```python
from iodd_parser import IODDParser

parser = IODDParser()
result = parser.parse("path/to/device-IODD1.1.zip")

var = result.variables["V_DeviceStatus"]
if hasattr(var.datatype, "single_values"):
    for sv in var.datatype.single_values:
        print(f"  {sv.value}: {sv.name}")
        # Output:
        #   0: Device is OK
        #   1: Maintenance required
        #   2: Out of specification
```

#### User Interface

The user interface defines how the device is presented in IO-Link Tools:

- **`ResolvedUserInterface`**: Contains menus and three role-based menu sets
- **`ResolvedMenuSet`**: Top-level menu references for a user role (Identification, Parameter, Observation, Diagnosis)
- **`ResolvedMenu`**: A menu containing variable refs, record item refs, and sub-menu refs
- **`ResolvedVariableRef`**: Reference to a variable with display options (gradient, offset, unit, format)
- **`ResolvedRecordItemRef`**: Reference to a record item with subindex
- **`ResolvedMenuRef`**: Reference to a sub-menu with optional condition
- **`ResolvedCondition`**: Condition for conditional menu display

```python
# Access user interface menus
ui = result.user_interface

# Get the specialist role menu set
specialist = ui.specialist_role_menu_set
print(f"Identification menu: {specialist.identification_menu_id}")

# Access menu details
menu = ui.menus[specialist.identification_menu_id]
for var_ref in menu.variable_refs:
    print(f"  Variable: {var_ref.variable_id}")
```

## Licence

Everything except `src/iodd_parser/generated/` and `src/iodd_parser/standard_definitions/` is licensed under the MIT licence.

The files in `generated/` and `standard_definitions/` are derived from the IO-Link specification and are subject to the IO-Link Community licensing terms.
