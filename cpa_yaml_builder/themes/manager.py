import yaml
from typing import Dict
from utils.loader import load_yaml_file

class ThemeManager:
    def __init__(self, theme_file: str = "user_defaults.yaml"):
        self.theme_data = load_yaml_file(theme_file)

    def apply(self, control_type: str, props: Dict, mode: str = "static") -> Dict:
        """
        Merge theme properties with user-defined properties.
        Priority: theme < control default < user input
        """
        theme_props = self.theme_data.get(control_type, {})

        if mode == "powerfx-object":
            themed = {k: f"AppTheme.{control_type}.{k}" for k in theme_props}
        elif mode == "powerfx":
            themed = {k: f"AppTheme_{control_type}_{k}" for k in theme_props}
        else:
            themed = theme_props

        return {**themed, **props}
