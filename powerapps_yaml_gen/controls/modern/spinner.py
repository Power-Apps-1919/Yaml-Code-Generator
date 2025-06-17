from controls.base import BaseControl
from control_factory import register_control

@register_control("Spinner", control_family="modern")
class SpinnerControl(BaseControl):
    def get_control_name(self):
        return "Modern/Spinner"

    def get_default_properties(self):
        return {
            # General
            "Label": '"Loading..."',
            "AccessibleLabel": '"Spinner control"',
            "Visible": True,
            # Size and position
            "LabelPosition": '"Top"',
            "SpinnerSize": '"Medium"',
            "X": 0,
            "Y": 0,
            "Width": 48,
            "Height": 48,
            # Style and theme
            "Appearance": '"Primary"',
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
            "OnChange": ""
        }
