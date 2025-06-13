from controls.base import BaseControl
from control_factory import register_control

@register_control("Video", control_family="classic")
class VideoControl(BaseControl):
    def get_control_name(self):
        return "Video"

    def get_default_properties(self):
        return {
            "AccessibleLabel": "\"Video player\"",
            "AutoPause": True,
            "AutoStart": False,
            "BorderColor": "=ColorFade(Self.Fill, -15%)",
            "BorderStyle":  "BorderStyle.Solid",
            "BorderThickness": 1,
            "ClosedCaptionsUrl": "\"\"",
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "=RGBA(255, 255, 255, 1)",
            "FocusedBorderColor": "=ColorFade(Self.Fill, -15%)",
            "FocusedBorderThickness": 2,
            "Height": 40,
            "Image": "\"\"",
            "ImagePosition": "ImagePosition.Left",
            "Loop": False,
            "Media": "SampleVideo",
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