from controls.base import BaseControl
from control_factory import register_control

@register_control("DropDown", control_family="classic")
class DropDownControl(BaseControl):
    def get_control_name(self):
        return "Classic/DropDown"

    def get_default_properties(self):
        return {
            # Key properties
            "Default": "1",
            "Items": "DropDownSample",
            "Value": "Value",
            "Selected": '{}',
            "AllowEmptySelection": False,
            "AccessibleLabel": "\"Drop down\"",
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "ChevronBackground": "=RGBA(255,255,255,1)",
            "ChevronFill": "=RGBA(56, 96, 178, 1)",
            "Color": "=RGBA(0,0,0,1)",
            "DisplayMode": "DisplayMode.Edit",
            "DisabledBorderColor": "=RGBA(166,166,166,1)",
            "DisabledColor": "=RGBA(166,166,166,1)",
            "DisabledFill": "=RGBA(244,244,244,1)",
            "Fill": "=RGBA(255,255,255,1)",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "Font": "=Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Height": 44,
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "HoverColor": "=RGBA(0,0,0,1)",
            "HoverFill": "=RGBA(237,244,252,1)",
            "Italic": False,
            "OnChange": "",
            "OnSelect": "",
            "PaddingBottom": 5,
            "PaddingLeft": 8,
            "PaddingRight": 8,
            "PaddingTop": 5,
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "PressedColor": "=RGBA(0,0,0,1)",
            "PressedFill": "=RGBA(204,228,247,1)",
            "Reset": False,
            "SelectionColor": "=RGBA(56, 96, 178, 1)",
            "SelectionFill": "=RGBA(237,244,252,1)",
            "Size": 14,
            "Strikethrough": False,
            "TabIndex": 0,
            "Tooltip": "\"Select an option\"",
            "Underline": False,
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
