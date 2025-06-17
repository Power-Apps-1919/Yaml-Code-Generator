from controls.base import BaseControl
from control_factory import register_control

@register_control("TabList", control_family="modern")
class TabListControl(BaseControl):
    def get_control_name(self):
        return "Modern/TabList"

    def get_default_properties(self):
        return {
            # General
            "Items": '["Tab 1", "Tab 2", "Tab 3"]',
            "AccessibleLabel": '"Tab list control"',
            "Visible": True,
            # Behavior
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "Size": '"Medium"',
            "Alignment": '"Horizontal"',
            "X": 0,
            "Y": 0,
            "Width": 300,
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
            "DefaultSelectedItems": '["Tab 1"]',
            "OnChange": "",
            "OnSelect": ""
        }
