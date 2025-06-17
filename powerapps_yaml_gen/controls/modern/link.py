from controls.base import BaseControl
from control_factory import register_control

@register_control("Link", control_family="modern")
class LinkControl(BaseControl):
    def get_control_name(self):
        return "Modern/Link"

    def get_default_properties(self):
        return {
            # General
            "Text": '"Click here"',
            "URL": '"https://example.com"',
            "AccessibleLabel": '"Link control"',
            "Visible": True,
            # Behavior
            "Wrap": True,
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "Align": '"Start"',
            "VerticalAlign": '"Center"',
            "AutoHeight": False,
            "X": 0,
            "Y": 0,
            "Width": 200,
            "Height": 32,
            # Style and theme
            "BasePaletteColor": '"ThemePrimary"',
            "Font": '"Segoe UI"',
            "FontSize": 14,
            "FontWeight": '"Normal"',
            "FontItalic": False,
            "FontStrikethrough": False,
            "FontUnderline": True,
            # Additional properties
            "AcceptsFocus": True
        }
