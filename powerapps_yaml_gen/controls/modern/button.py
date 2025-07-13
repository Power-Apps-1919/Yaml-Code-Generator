from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("Button", control_family="modern")
class ButtonControl(BaseControl):
    def get_control_name(self):
        return "Modern/Button"

    def get_default_properties(self):
        return {
            # General
            "Text": '"Button"',
            "AccessibleLabel": '"Button control"',
            "Visible": True,
            # Icon
            "Icon": '"None"',
            "Layout": '"IconLeft"',
            "IconRotation": 0,
            "IconStyle": '"Filled"',
            # Behavior
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 120,
            "Height": 40,
            # Style and theme
            "Appearance": '"Primary"',
            "BasePaletteColor": '"ThemePrimary"',
            "Font": '"Segoe UI"',
            "FontSize": 16,
            "FontColor": '"#000000"',
            "FontWeight": '"Normal"',
            "FontItalic": False,
            "FontUnderline": False,
            "FontStrikethrough": False,
            # Additional properties
            "AcceptsFocus": True,
            "OnSelect": ""
        }
