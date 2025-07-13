from cpa_yaml_builder.controls.base import BaseControl
from cpa_yaml_builder.control_factory import register_control

@register_control("PenInput", control_family="classic")
class PenInputControl(BaseControl):
    def get_control_name(self):
        return "Classic/PenInput"

    def get_default_properties(self):
        return {
            # Key properties
            "Color": "=RGBA(56, 96, 178, 1)",
            "Mode": "PenInputMode.Draw",
            # Additional properties
            "AccessibleLabel": '"Pen input"',
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "=RGBA(255,255,255,1)",
            "Height": 150,
            "Input": 7,  # Deprecated, supports all inputs
            "OnSelect": "",
            "SelectionColor": "=RGBA(56, 96, 178, 1)",
            "SelectionThickness": 2,
            "ShowControls": True,
            "Size": 14,
            "Tooltip": '"Draw or sign here"',
            "Visible": True,
            "Width": 300,
            "X": 0,
            "Y": 0
        }
