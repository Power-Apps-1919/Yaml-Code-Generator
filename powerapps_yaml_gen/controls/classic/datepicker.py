from controls.base import BaseControl
from control_factory import register_control

@register_control("DatePicker", control_family="classic")
class DatePickerControl(BaseControl):
    def get_control_name(self):
        return "Classic/DatePicker"

    def get_default_properties(self):
        return {
            "AccessibleLabel": "\"Date picker\"",
            "BorderColor": "=ColorFade(Self.Fill, -15%)",
            "BorderRadius": 2,
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "Color": "=RGBA(0, 0, 0, 1)",
            "ContentLanguage": "=Language()",
            "DateTimeZone": "DateTimeZone.Local",
            "DefaultDate": "=Today()",
            "DisplayMode": "DisplayMode.Edit",
            "DisabledBorderColor": "=RGBA(166, 166, 166, 1)",
            "DisabledColor": "=RGBA(166, 166, 166, 1)",
            "DisabledFill": "=RGBA(240, 240, 240, 1)",
            "EndYear": 2100,
            "Fill": "=RGBA(255, 255, 255, 1)",
            "FocusedBorderColor": "=ColorFade(Self.Fill, -15%)",
            "FocusedBorderThickness": 2,
            "Font": "=Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Height": 40,
            "IconFill": "=Self.Color",
            "IconBackground": "=Self.Fill",
            "InputTextPlaceholder": "\"Select a date\"",
            "IsEditable": True,
            "Italic": False,
            "OnChange": "",
            "OnSelect": "",
            "PaddingBottom": 5,
            "PaddingLeft": 10,
            "PaddingRight": 10,
            "PaddingTop": 5,
            "Reset": False,
            "Size": 14,
            "StartOfWeek": "StartOfWeek.Monday",
            "StartYear": 1900,
            "TabIndex": 0,
            "Tooltip": "\"Tooltip\"",
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
