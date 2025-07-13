# Power Apps YAML Generator

A simple tool to generate YAML configuration files for Power Apps controls, making it easier to manage and share control settings.

## Features
- Generate YAML for Power Apps controls
- Supports default and custom property values
- Easily extendable for new controls

## Installation
1. Clone this repository.
2. Install dependencies with:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Import and use the builder in your Python scripts:
```python
from builder import call_yaml_gen

yaml_str = call_yaml_gen('Label', 'label1', options={"Text": '"Hello!"'}, with_defaults=True)
print(yaml_str)
```

## Adding New Controls
- Add a new Python file in `controls/classic/` or `controls/modern/`.
- Register your control with the `@register_control` decorator.
- Define default properties in `get_default_properties()`.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
