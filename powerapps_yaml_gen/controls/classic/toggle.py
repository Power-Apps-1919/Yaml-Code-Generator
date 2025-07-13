from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("Toggle", control_family="classic")
class ToggleControl(BaseControl):
    def get_control_name(self):
        return "Classic/Toggle"

    def get_default_properties(self):
        return {
            # Key properties
            "Default": False,
            "Value": False,
            # Additional properties
            "AccessibleLabel": '"Toggle control"',
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "DisabledBorderColor": "=RGBA(166,166,166,1)",
            "FalseFill": "=RGBA(244,244,244,1)",
            "FalseHoverFill": "=RGBA(237,244,252,1)",
            "FalseText": '"Off"',
            "Fill": "=RGBA(255,255,255,1)",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "HandleFill": "=RGBA(56, 96, 178, 1)",
            "Height": 32,
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "OnChange": "",
            "OnCheck": "",
            "OnSelect": "",
            "OnUncheck": "",
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "RailFill": "=RGBA(204,228,247,1)",
            "RailHoverFill": "=RGBA(237,244,252,1)",
            "Reset": False,
            "ShowLabel": True,
            "TabIndex": 0,
            "TextPosition": "TextPosition.Right",
            "Tooltip": '"Toggle on/off"',
            "TrueFill": "=RGBA(56, 96, 178, 1)",
            "TrueHoverFill": "=RGBA(0,120,212,1)",
            "TrueText": '"On"',
            "ValueFill": "=RGBA(56, 96, 178, 1)",
            "ValueHoverFill": "=RGBA(0,120,212,1)",
            "Visible": True,
            "Width": 80,
            "X": 0,
            "Y": 0
        }
