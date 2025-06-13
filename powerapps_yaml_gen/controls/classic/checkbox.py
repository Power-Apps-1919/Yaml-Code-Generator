from controls.base import BaseControl
from control_factory import register_control

@register_control("CheckBox", control_family="classic")
class CheckBoxControl(BaseControl):
    def get_control_name(self):
        return "Classic/CheckBox"

    def get_default_properties(self):
        return {
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "CheckboxBackgroundFill": "=RGBA(255,255,255,1)",
            "CheckboxBorderColor": "=RGBA(56, 96, 178, 1)",
            "CheckboxSize": 20,
            "CheckmarkFill": "=RGBA(56, 96, 178, 1)",
            "Color": "=RGBA(0,0,0,1)",
            "Default": False,
            "DisabledBorderColor": "=RGBA(166,166,166,1)",
            "DisabledColor": "=RGBA(166,166,166,1)",
            "DisabledFill": "=RGBA(244,244,244,1)",
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "=RGBA(255,255,255,1)",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "Font": "=Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Height": 40,
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "HoverColor": "=RGBA(0,0,0,1)",
            "HoverFill": "=RGBA(237,244,252,1)",
            "Italic": False,
            "OnCheck": "",
            "OnSelect": "",
            "OnUncheck": "",
            "PaddingBottom": 5,
            "PaddingLeft": 8,
            "PaddingRight": 8,
            "PaddingTop": 5,
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "PressedColor": "=RGBA(0,0,0,1)",
            "PressedFill": "=RGBA(204,228,247,1)",
            "Reset": False,
            "Size": 14,
            "Strikethrough": False,
            "TabIndex": 0,
            "Text": "Check me",
            "Tooltip": '"Check this box"',
            "Underline": False,
            "Value": False,
            "VerticalAlign": "VerticalAlign.Middle",
            "Visible": True,
            "Width": 120,
            "X": 0,
            "Y": 0
        }
