from controls.base import BaseControl
from control_factory import register_control

@register_control("Button", control_family="classic")
class ButtonControl(BaseControl):
    def get_control_name(self):
        return "Classic/Button"

    def get_default_properties(self):
        return {
            "Text": "\"Button\"",
            "X": 0,
            "Y": 0,
            "Width": 100,
            "Height": 40,
            "Visible": True,
            "Color": "RGBA(0, 0, 0, 1)",
            "Fill": "RGBA(255, 255, 255, 1)",
            "Font": "Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Size": 14,
            "PaddingTop": 5,
            "PaddingRight": 10,
            "PaddingBottom": 5,
            "PaddingLeft": 10,
            "Align": "Align.Center",
            "VerticalAlign": "VerticalAlign.Middle",
            "BorderColor": "RGBA(0, 0, 0, 0)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "HoverColor": "RGBA(0, 0, 0, 1)",
            "HoverFill": "RGBA(240, 240, 240, 1)",
            "PressedColor": "RGBA(0, 0, 0, 1)",
            "PressedFill": "RGBA(200, 200, 200, 1)",
            "FocusedBorderColor": "RGBA(0, 0, 0, 1)",
            "FocusedBorderThickness": 2,
            "DisabledColor": "RGBA(128, 128, 128, 1)",
            "DisabledFill": "RGBA(240, 240, 240, 1)",
            "TabIndex": 0,
            "Tooltip": "\"Tooltip\"",
            "OnSelect": False
        }