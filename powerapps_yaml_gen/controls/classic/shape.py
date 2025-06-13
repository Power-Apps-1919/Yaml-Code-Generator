from controls.base import BaseControl
from control_factory import register_control

@register_control("Shape", control_family="classic")
class ShapeControl(BaseControl):
    def get_control_name(self):
        return "Classic/Shape"

    def get_default_properties(self):
        return {
            # Key properties (shapes)
            "Fill": "=RGBA(56, 96, 178, 1)",
            "OnSelect": "",
            # Additional properties
            "AccessibleLabel": '"Shape"',
            "DisplayMode": "DisplayMode.Edit",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "Height": 32,
            "HoverFill": "=RGBA(237,244,252,1)",
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "PressedFill": "=RGBA(204,228,247,1)",
            "TabIndex": 0,
            "Visible": True,
            "Width": 32,
            "X": 0,
            "Y": 0
        }
