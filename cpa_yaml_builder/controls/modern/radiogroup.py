from cpa_yaml_builder.controls.base import BaseControl
from cpa_yaml_builder.control_factory import register_control

@register_control("RadioGroup", control_family="modern")
class RadioGroupControl(BaseControl):
    def get_control_name(self):
        return "Modern/RadioGroup"

    def get_default_properties(self):
        return {
            # General
            "Items": '["Option 1", "Option 2", "Option 3"]',
            "AccessibleLabel": '"Radio group control"',
            "Visible": True,
            # Behavior
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "Layout": '"Vertical"',
            "X": 0,
            "Y": 0,
            "Width": 200,
            "Height": 40,
            # Style and theme
            "BasePaletteColor": '"ThemePrimary"',
            "Font": '"Segoe UI"',
            "FontSize": 14,
            "FontColor": '"#000000"',
            "FontWeight": '"Normal"',
            "FontItalic": False,
            "FontUnderline": False,
            "FontStrikethrough": False,
            # Additional properties
            "DefaultSelectedItems": '"Option 1"',
            "OnChange": "",
            "OnSelect": ""
        }
