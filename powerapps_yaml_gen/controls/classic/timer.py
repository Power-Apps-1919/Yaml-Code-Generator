from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("Timer", control_family="classic")
class TimerControl(BaseControl):
    def get_control_name(self):
        return "Classic/Timer"

    def get_default_properties(self):
        return {
            # Key properties
            "Duration": 60000,  # 60 seconds in ms
            "OnTimerEnd": "",
            "Repeat": False,
            # Additional properties
            "Align": "Align.Center",
            "AutoPause": True,
            "AutoStart": False,
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
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "HoverColor": "=RGBA(0,0,0,1)",
            "HoverFill": "=RGBA(237,244,252,1)",
            "Italic": False,
            "OnSelect": "",
            "OnTimerStart": "",
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "PressedColor": "=RGBA(0,0,0,1)",
            "PressedFill": "=RGBA(204,228,247,1)",
            "Reset": False,
            "Size": 14,
            "Start": False,
            "Strikethrough": False,
            "TabIndex": 0,
            "Text": '"Timer"',
            "Tooltip": '"Timer control"',
            "Underline": False,
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
