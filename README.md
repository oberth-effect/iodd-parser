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
result = parser.parse("path/to/device-IODD1.1.zip")

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

### Language Support

The parser supports multiple languages for text resolution. Language-specific standard
definition files are pre-loaded at parser initialisation, and device-specific language
files are loaded automatically from the IODD ZIP archive.

```python
from iodd_parser import IODDParser

# Pre-load German language definitions
parser = IODDParser(langs=["de", "fr"])

# Parse with German texts
result = parser.parse("path/to/device-IODD1.1.zip", lang="de")

# Variable names are now in German
print(result.variables["V_VendorName"].name)  # "Herstellername"
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

The `parse()` method returns a `ParsedIODD` object containing:

```python
@dataclass
class ParsedIODD:
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
    datatypes: dict[str, DatatypeT]             # Keyed by datatype ID
    errors: dict[tuple[int, int], ResolvedError]  # Keyed by (code, additional_code)
    units: dict[int, ResolvedUnit]              # Keyed by unit code

    # Extracted images (if load_images=True)
    images: list[IoddImage]
```

### Resolved Types

- **`ResolvedVariable`**: Variables from StdVariableRef, DirectParameterOverlay, or vendor-specific Variable elements
- **`ResolvedError`**: Error types (code=128 for standard, code=129 for vendor-specific)
- **`ResolvedUnit`**: Unit definitions with code, abbreviation, and name
- **`ResolvedProcessData`**: Process data configuration with optional condition for switching
- **`ResolvedProcessDataItem`**: Individual process data input/output description

## Licence

Everything except `src/iodd_parser/generated/` and `src/iodd_parser/standard_definitions/` is licensed under the MIT licence.

The files in `generated/` and `standard_definitions/` are derived from the IO-Link specification and are subject to the IO-Link Community licensing terms.
