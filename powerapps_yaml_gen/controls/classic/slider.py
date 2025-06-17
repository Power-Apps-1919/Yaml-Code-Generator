from controls.base import BaseControl
from control_factory import register_control

@register_control("Slider", control_family="classic")
class SliderControl(BaseControl):
    def get_control_name(self):
        return "Classic/Slider"

    def get_default_properties(self):
        return {
            # Key properties
            "Default": 0,
            "Max": 100,
            "Min": 0,
            "Value": 0,
            # Additional properties
            "AccessibleLabel": '"Slider control"',
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "DisabledBorderColor": "=RGBA(166,166,166,1)",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "HandleActiveFill": "=RGBA(56, 96, 178, 1)",
            "HandleFill": "=RGBA(255,255,255,1)",
            "HandleHoverFill": "=RGBA(237,244,252,1)",
            "HandleSize": 20,
            "Height": 44,
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "Layout": "Layout.Horizontal",
            "OnChange": "",
            "OnSelect": "",
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "RailFill": "=RGBA(204,228,247,1)",
            "RailHoverFill": "=RGBA(237,244,252,1)",
            "ReadOnly": False,
            "Reset": False,
            "ShowValue": True,
            "TabIndex": 0,
            "Tooltip": '"Adjust the value"',
            "ValueFill": "=RGBA(56, 96, 178, 1)",
            "ValueHoverFill": "=RGBA(0,120,212,1)",
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
