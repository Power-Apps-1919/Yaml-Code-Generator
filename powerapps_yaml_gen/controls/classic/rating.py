from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("Rating", control_family="classic")
class RatingControl(BaseControl):
    def get_control_name(self):
        return "Classic/Rating"

    def get_default_properties(self):
        return {
            # Key properties
            "Default": 0,
            "Max": 5,
            # Additional properties
            "AccessibleLabel": '"Rating control"',
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "Fill": "=RGBA(255,255,255,1)",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "Height": 44,
            "OnChange": "",
            "OnSelect": "",
            "RatingFill": "=RGBA(255, 205, 0, 1)",
            "ReadOnly": False,
            "Reset": False,
            "ShowValue": True,
            "TabIndex": 0,
            "Tooltip": '"Rate this item"',
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
