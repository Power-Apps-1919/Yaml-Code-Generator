from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("CheckBox", control_family="modern")
class CheckBoxControl(BaseControl):
    def get_control_name(self):
        return "Modern/CheckBox"

    def get_default_properties(self):
        return {
            # General
            "Label": '"Check me"',
            "AccessibleLabel": '"Checkbox control"',
            "Visible": True,
            # Behavior
            "Checked": False,
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 120,
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
            "OnCheck": "",
            "OnSelect": "",
            "OnUncheck": ""
        }
