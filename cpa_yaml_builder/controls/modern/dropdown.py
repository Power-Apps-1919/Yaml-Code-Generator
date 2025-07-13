from cpa_yaml_builder.controls.base import BaseControl
from cpa_yaml_builder.control_factory import register_control

@register_control("DropDown", control_family="modern")
class DropDownControl(BaseControl):
    def get_control_name(self):
        return "Modern/DropDown"

    def get_default_properties(self):
        return {
            # General
            "Items": "DropDownSample",
            "AccessibleLabel": '"Drop down control"',
            "Visible": True,
            # Behavior
            "Required": False,
            "DisplayMode": "DisplayMode.Edit",
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 200,
            "Height": 40,
            # Style and theme
            "BasePaletteColor": '"ThemePrimary"',
            "FontSize": 14,
            # Additional properties
            "OnChange": "",
            "ValidationState": '"None"',
            "DefaultSelectedItems": '[]'
        }
