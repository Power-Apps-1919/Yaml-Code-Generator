from controls.base import BaseControl
from control_factory import register_control

@register_control("Camera", control_family="classic")
class CameraControl(BaseControl):
    def get_control_name(self):
        return "Camera"

    def get_default_properties(self):
        return {
            "Camera": 0,  # Camera ID
            "AccessibleLabel": "\"Camera control\"",
            "BorderColor": "=ColorFade(Self.Fill, -15%)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "Brightness": 0,
            "Contrast": 0,
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "=RGBA(255, 255, 255, 1)",
            "FocusedBorderColor": "=ColorFade(Self.Fill, -15%)",
            "FocusedBorderThickness": 2,
            "Height": 200,
            "OnChange": "",
            "OnPhoto": "",
            "OnSelect": "",
            "OnStream": "",
            "Photo": "",
            "Stream": False,
            "StreamRate": 1000,
            "TabIndex": 0,
            "Tooltip": "\"Take a photo\"",
            "Visible": True,
            "Width": 300,
            "X": 0,
            "Y": 0
        }
