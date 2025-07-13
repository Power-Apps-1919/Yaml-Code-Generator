from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("NumberInput", control_family="modern")
class NumberInputControl(BaseControl):
    def get_control_name(self):
        return "Modern/NumberInput"

    def get_default_properties(self):
        return {
            # General
            "Value": 0,
            "Min": 0,
            "Max": 100,
            "Precision": 0,
            "Step": 1,
            "AccessibleLabel": '"Number input control"',
            "Visible": True,
            # Behavior
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 120,
            "Height": 40,
            # Style and theme
            "BasePaletteColor": '"ThemePrimary"',
            "FontSize": 14,
            "Align": '"Start"',
            # Additional properties
            "DelayOutput": False,
            "OnChange": "",
            "ValidationState": '"None"'
        }
