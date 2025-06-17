from controls.base import BaseControl
from control_factory import register_control

@register_control("Radio", control_family="classic")
class RadioControl(BaseControl):
    def get_control_name(self):
        return "Classic/Radio"

    def get_default_properties(self):
        return {
            # Key properties
            "Default": '"Option1"',
            "Items": "RadioSample",
            "Layout": "Layout.Vertical",
            "Value": '"Value"',
            "Selected": '{}',
            # All properties
            "Align": "Align.Left",
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
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
            "HoverColor": "=RGBA(0,0,0,1)",
            "HoverFill": "=RGBA(237,244,252,1)",
            "Italic": False,
            "LineHeight": 1.2,
            "OnChange": "",
            "OnSelect": "",
            "PaddingBottom": 5,
            "PaddingLeft": 8,
            "PaddingRight": 8,
            "PaddingTop": 5,
            "PressedColor": "=RGBA(0,0,0,1)",
            "PressedFill": "=RGBA(204,228,247,1)",
            "RadioBackgroundFill": "=RGBA(255,255,255,1)",
            "RadioBorderColor": "=RGBA(56, 96, 178, 1)",
            "RadioSelectionFill": "=RGBA(56, 96, 178, 1)",
            "RadioSize": 20,
            "Reset": False,
            "SelectedText": '"Option1"',  # Deprecated
            "Size": 14,
            "Strikethrough": False,
            "TabIndex": 0,
            "Tooltip": '"Select an option"',
            "Underline": False,
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
