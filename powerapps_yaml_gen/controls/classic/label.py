from controls.base import BaseControl
from control_factory import register_control

@register_control("Label", control_family="classic")
class LabelControl(BaseControl):
    def get_control_name(self):
        return "Label"
    def get_default_properties(self):
        return {
            "Align": "Align.Left",
            "AutoHeight": False,
            "BorderColor": "RGBA(0, 0, 0, 0)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 0,
            "Color": "RGBA(0, 0, 0, 1)",
            "ContentLanguage": "Language()",
            "DisabledBorderColor": "RGBA(0, 0, 0, 0)",
            "DisabledColor": "RGBA(128, 128, 128, 1)",
            "DisabledFill": "RGBA(240, 240, 240, 1)",
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "RGBA(255, 255, 255, 1)",
            "FocusedBorderColor": "RGBA(0, 0, 0, 1)",
            "FocusedBorderThickness": 1,
            "Font": "Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Height": 30,
            "HoverBorderColor": "RGBA(0, 0, 0, 0)",
            "HoverColor": "RGBA(0, 0, 0, 1)",
            "HoverFill": "RGBA(240, 240, 240, 1)",
            "Italic": False,
            "LineHeight": 1.2,
            "Live": "Live.Assertive",
            "OnSelect": False,
            "PaddingBottom": 0,
            "PaddingLeft": 0,
            "PaddingRight": 0,
            "PaddingTop": 0,
            "PressedBorderColor": "RGBA(0, 0, 0, 0)",
            "PressedColor": "RGBA(0, 0, 0, 1)",
            "PressedFill": "RGBA(255, 255, 255, 1)",
            "Size": 12,
            "Strikethrough": False,
            "TabIndex": 0,
            "Text": "\"Text\"",
            "Tooltip": "\"Tooltip\"",
            "Underline": False,
            "VerticalAlign": "VerticalAlign.Middle",
            "Visible": True,
            "Width": 200,
            "Wrap": True,
            "X": 0,
            "Y": 0
        }
