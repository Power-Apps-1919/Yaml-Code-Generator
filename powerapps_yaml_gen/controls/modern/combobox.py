from controls.base import BaseControl
from control_factory import register_control

@register_control("ComboBox", control_family="modern")
class ComboBoxControl(BaseControl):
    def get_control_name(self):
        return "Modern/ComboBox"

    def get_default_properties(self):
        return {
            # General
            "Items": "ComboBoxSample",
            "AccessibleLabel": '"Combo box control"',
            "Visible": True,
            # Behavior
            "SelectMultiple": False,
            "IsSearchable": True,
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
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
            "OnChange": "",
            "TextInputPlaceholder": '"Select an item"',
            "MultiValueDelimiter": '","',
            "ValidationState": '"None"',
            "DefaultSelectedItems": '[]'
        }
