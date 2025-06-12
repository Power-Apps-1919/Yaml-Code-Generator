from controls.base import BaseControl
from control_factory import register_control

@register_control("Label", control_family="classic")
class LabelControl(BaseControl):
    def get_control_name(self):
        return "Label"
    def get_default_properties(self):
        return {
            "Text": "\"Text\"",
            "ContentLanguage": "Language()",
            "Live": "Live.Assertive",
            "X": 0,
            "Y": 0,
            "Width": 200,
            "Height": 30,
            "Visible": True,
            "Color": "RGBA(0, 0, 0, 1)",
            "Fill": "RGBA(255, 255, 255, 1)",
            "Font": "Font.'Open Sans'",
            "FontWeight": "FontWeight.Normal",
            "Size": 12,
            "PaddingTop": 0,
            "PaddingRight": 0,
            "PaddingBottom": 0,
            "PaddingLeft": 0,
            "Align": "Align.Left",
            "VerticalAlign": "VerticalAlign.Middle",
            "Wrap": True,
            "BorderColor": "RGBA(0, 0, 0, 0)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 0,
            "DisplayMode": "DisplayMode.Edit",
            "HoverColor": "RGBA(0, 0, 0, 1)",
            "HoverFill": "RGBA(240, 240, 240, 1)",
            "HoverBorderColor": "RGBA(0, 0, 0, 0)",
            "PressedColor": "RGBA(0, 0, 0, 1)",
            "PressedFill": "RGBA(255, 255, 255, 1)",
            "PressedBorderColor": "RGBA(0, 0, 0, 0)",
            "FocusedBorderColor": "RGBA(0, 0, 0, 1)",
            "FocusedBorderThickness": 1,
            "DisabledColor": "RGBA(128, 128, 128, 1)",
            "DisabledFill": "RGBA(240, 240, 240, 1)",
            "DisabledBorderColor": "RGBA(0, 0, 0, 0)",
            "TabIndex": 0,
            "Tooltip": "\"Tooltip\"",
            "Italic": False,
            "Underline": False,
            "Strikethrough": False,
            "AutoHeight": False,
            "LineHeight": 1.2,
            "Align": "Align.Left",
            "OnSelect": False
        }