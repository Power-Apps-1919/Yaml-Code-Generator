from controls.base import BaseControl
from control_factory import register_control

@register_control("ComboBox", control_family="classic")
class ComboBoxControl(BaseControl):
    def get_control_name(self):
        return "Classic/ComboBox"

    def get_default_properties(self):
        return {
            "Items": "ComboBoxSample",  
            "DefaultSelectedItems": "[]",
            "SelectedItems": "[]",
            "Selected": "{}",
            "SelectMultiple": False,
            "IsSearchable": True,
            "SearchFields": '["Name"]',
            "AccessibleLabel": '"Combo box"',
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayFields": '["Name"]',
            "DisplayMode": "DisplayMode.Edit",
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "Height": 44,
            "InputTextPlaceholder": '"Select an item"',
            "OnChange": "",
            "OnNavigate": "",
            "OnSelect": "",
            "TabIndex": 0,
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
