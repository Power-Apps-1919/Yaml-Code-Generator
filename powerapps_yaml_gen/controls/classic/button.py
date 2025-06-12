from controls.base import BaseControl
from control_factory import register_control

@register_control("Button", control_family="classic")
class ButtonControl(BaseControl):
    def get_control_name(self):
        return "Classic/Button"

    def get_default_properties(self):
        return {
            "Text": "\"Button\"",
            "OnSelect": False,
            "Align": "Align.Center",
            "AutoDisableOnSelect": True,
            "BorderColor": "=ColorFade(Self.Fill, -15%)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "Color": "=RGBA(255, 255, 255, 1)",
            "ContentLanguage": "=Language()",
            "DisplayMode": "DisplayMode.Edit",
            "DisabledBorderColor": "=RGBA(166, 166, 166, 1)",
            "DisabledColor": "=RGBA(166, 166, 166, 1)",
            "DisabledFill": "=RGBA(240, 240, 240, 1)",
            "FocusedBorderColor": "=ColorFade(Self.Fill, -15%)",
            "FocusedBorderThickness": 2,
            "Fill": "=RGBA(56, 96, 178, 1)",
            "Font": "=Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Height": 40,
            "HoverBorderColor": "=ColorFade(Self.BorderColor, 20%)",
            "HoverColor": "=RGBA(255, 255, 255, 1)",
            "HoverFill": "=ColorFade(RGBA(56, 96, 178, 1), -20%)",
            "Italic": False,
            "PaddingBottom": 5,
            "PaddingLeft": 10,
            "PaddingRight": 10,
            "PaddingTop": 5,
            "PressedBorderColor": "=Self.Fill",
            "PressedColor": "=Self.Fill",
            "PressedFill": "=Self.Color",
            "RadiusBottomLeft": 2,
            "RadiusBottomRight": 2,
            "RadiusTopLeft": 2, 
            "RadiusTopRight": 2,
            "Size": 14,
            "Strikethrough": False,
            "TabIndex": 0,
            "Tooltip": "\"Tooltip\"",
            "Underline": False,
            "VerticalAlign": "VerticalAlign.Middle",
            "Visible": True,
            "Width": 100,
            "X": "=190",
            "Y": "=185"  
        }