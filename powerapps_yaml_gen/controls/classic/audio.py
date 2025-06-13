from controls.base import BaseControl
from control_factory import register_control

@register_control("Audio", control_family="classic")
class AudioControl(BaseControl):
    def get_control_name(self):
        return "Audio"

    def get_default_properties(self):
        return {
            "AccessibleLabel": "\"Audio player\"",
            "AutoPause": True,
            "AutoStart": False,
            "BorderColor": "=ColorFade(Self.Fill, -15%)",
            "BorderStyle":  "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "=RGBA(255, 255, 255, 1)",
            "FocusedBorderColor": "=ColorFade(Self.Fill, -15%)",
            "FocusedBorderThickness": 2,
            "Height": 40,
            "Image": "\"\"",
            "ImagePosition": "ImagePosition.Left",
            "Loop": False,
            "Media": "SampleAudio",
            "Onend": "",
            "OnPause": "",
            "OnPlay": "",
            "Paused": False,
            "Reset": False,
            "ShowControls": True,
            "Start": False,
            "StartTime": 0,
            "Time":  0,
            "TabIndex": 0,
            "Tooltip": "\"Tooltip\"",
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0,
        }