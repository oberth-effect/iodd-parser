# IODD Parser

A very basic python package for parsing [IO Device Description](https://ioddfinder.io-link.com/) v1.1 files.

It is nothing more than a convenience wrapper around a parser created using [`xsdata`](https://github.com/tefra/xsdata)
from the `.xsd` schema files (excluding the Snippets schema)
from [the IOLink Specification](https://io-link.com/downloads).

## Usage

```python
from iodd_parser import IODDParser

IODDParser().parse("path/to/IODD1.1.zip")
```

returns a result object of:

```python
@dataclass
class ParsedIODD:
    iodd_definitions: IoddstandardDefinitions  # Standard Definitions as parsed according to the schema
    iodd_units: IoddstandardUnitDefinitions  # Standard Units Definitions as parsed according to the schema
    iodd_device: Iodevice  # IO Device Description as parsed according to the schema

    # variables: list[Variable]
    images: list[IoddImage]
    # texts: dict[str, str]
```

## Licence

Everything except `src/iodd_parser/generated` and `src/iodd_parser/standard_definitions/` is licenced under the MIT
licence.