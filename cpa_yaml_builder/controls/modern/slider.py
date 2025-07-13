from cpa_yaml_builder.controls.base import BaseControl
from cpa_yaml_builder.control_factory import register_control

@register_control("Slider", control_family="modern")
class SliderControl(BaseControl):
    def get_control_name(self):
        return "Modern/Slider"

    def get_default_properties(self):
        return {
            # General
            "Value": 0,
            "Min": 0,   
            "Max": 100,
            "AccessibleLabel": '"Slider control"',
            "Visible": True,
            # Behavior
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "Layout": '"Horizontal"',
            "Size": '"Medium"',
            "X": 0,
            "Y": 0,
            "Width": 200,
            "Height": 32,
            # Style and theme
            "BasePaletteColor": '"ThemePrimary"',
            # Additional properties
            "OnChange": ""
        }
