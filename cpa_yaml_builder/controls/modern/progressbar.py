from cpa_yaml_builder.controls.base import BaseControl
from cpa_yaml_builder.control_factory import register_control

@register_control("ProgressBar", control_family="modern")
class ProgressBarControl(BaseControl):
    def get_control_name(self):
        return "Modern/ProgressBar"

    def get_default_properties(self):
        return {
            # General
            "Value": 0,
            "Max": 100,
            "AccessibleLabel": '"Progress bar control"',
            "Visible": True,
            # Behavior
            "Indeterminate": False,
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 200,
            "Height": 8,
            # Style and theme
            "ProgressColor": '"Brand"',
            "Thickness": '"Medium"',
            "Shape": '"Rounded"',
            "BasePaletteColor": '"ThemePrimary"',
            # Additional properties
            "OnChange": "",
            "DisplayMode": "DisplayMode.Edit"
        }
