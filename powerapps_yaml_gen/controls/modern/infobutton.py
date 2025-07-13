from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("InfoButton", control_family="modern")
class InfoButtonControl(BaseControl):
    def get_control_name(self):
        return "Modern/InfoButton"

    def get_default_properties(self):
        return {
            # General
            "Content": '"More information"',
            "AccessibleLabel": '"Info button"',
            "Visible": True,
            # Size and position
            "IconSize": '"Medium"',
            "X": 0,
            "Y": 0,
            "Width": 32,
            "Height": 32,
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
            "DisplayMode": "DisplayMode.Edit",
            "AcceptsFocus": True,
            "OnSelect": ""
        }
