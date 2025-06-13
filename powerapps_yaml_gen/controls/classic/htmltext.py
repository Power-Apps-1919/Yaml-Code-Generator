from controls.base import BaseControl
from control_factory import register_control

@register_control("HtmlText", control_family="classic")
class HtmlTextControl(BaseControl):
    def get_control_name(self):
        return "Classic/HtmlText"

    def get_default_properties(self):
        return {

            "Color": "=RGBA(0,0,0,1)",
            "Font": "=Font.'Open Sans'",
            "HtmlText": '"<b>Hello, world!</b>"',
            "AutoHeight": False,
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 0,
            "DisplayMode": "DisplayMode.View",
            "DisabledBorderColor": "=RGBA(166,166,166,1)",
            "DisabledFill": "=RGBA(244,244,244,1)",
            "Fill": "=RGBA(255,255,255,1)",
            "Height": 100,
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "OnSelect": "",
            "PaddingBottom": 5,
            "PaddingLeft": 8,
            "PaddingRight": 8,
            "PaddingTop": 5,
            "Size": 14,
            "Tooltip": '"HTML text block"',
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
