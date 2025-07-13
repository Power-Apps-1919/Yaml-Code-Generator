from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("Badge", control_family="modern")
class BadgeControl(BaseControl):
    def get_control_name(self):
        return "Modern/Badge"

    def get_default_properties(self):
        return {
            # Main properties
            "Content": '"Badge"',
            "Visible": True,
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 32,
            "Height": 24,
            # Style and theme
            "Appearance": '"Filled"',
            "Shape": '"Rounded"',
            "ThemeColor": '"Brand"',
            "BasePaletteColor": '"ThemePrimary"',
            "Font": '"Segoe UI"',
            "FontSize": 14,
            "FontColor": '"#000000"',
            "FontWeight": '"Normal"',
            "FontItalic": False,
            "FontUnderline": False,
            "FontStrikethrough": False,
            # Additional properties
            "AccessibleLabel": '"Badge label"',
            "DisplayMode": "DisplayMode.Edit"
        }
