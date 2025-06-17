from controls.base import BaseControl
from control_factory import register_control

@register_control("DatePicker", control_family="modern")
class DatePickerControl(BaseControl):
    def get_control_name(self):
        return "Modern/DatePicker"

    def get_default_properties(self):
        return {
            # General
            "PlaceHolder": '"Select a date"',
            "Format": '"Short"',
            "AccessibleLabel": '"Date picker control"',
            "Visible": True,
            # Behavior
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
            "Required": False,
            "EndDate": '"2025-12-31"',
            "IsEditable": True,
            "OnChange": "",
            "SelectedDate": '"2025-06-17"',
            "StartDate": '"2020-01-01"',
            "StartOfWeek": '"Sunday"',
            "ValidationState": '"None"'
        }
