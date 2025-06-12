import os
import yaml
from typing import Optional, Union
from control_factory import create_control
from control_factory import auto_import_controls
auto_import_controls()
# Optional: ThemeManager can be injected externally
from themes.manager import ThemeManager  # Make sure this exists even if stubbed
from utils.formatter import ensure_serializable

# Global theme manager (set externally in advanced usage)
theme_manager: Optional[ThemeManager] = None

def build_control_yaml(
    control_type: str,
    name: str,
    props: Optional[dict] = None,
    control_family: str = "classic",
    output_path: Optional[str] = None,
    overwrite: bool = True,
    theme_mode: str = "static",  # "static" | "powerfx" | "powerfx-object"
    theme_enabled: bool = False,
    ) -> str:
    """
    Generate YAML for a Power Apps control and optionally save it to a file.
    """
    props = props or {}
    control_family = control_family.lower()

    # Apply theme properties if theme support is enabled
    if theme_enabled and theme_manager:
        props = theme_manager.apply(control_type, props, mode=theme_mode)

    # Create the control instance
    control = create_control(control_type, name, props, control_family)

    # Generate YAML content
    raw = control.build()
    control_key, control_block = list(raw.items())[0]

    # Only format Properties
    formatted = {
        control_key: {
            "Control": control_block["Control"],
            "Properties": ensure_serializable(control_block["Properties"])
        }
    }

    yaml_content = yaml.dump(
        [formatted],
        sort_keys=False,
        default_flow_style=False
    )

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if os.path.exists(output_path) and not overwrite:
            with open(output_path, "a", encoding="utf-8") as f:
                f.write("\n" + yaml_content)
            print(f"➕ Appended to {output_path}")
        else:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(yaml_content)
            print(f"✅ Saved YAML to {output_path}")

    return yaml_content
