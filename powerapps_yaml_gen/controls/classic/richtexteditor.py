from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("RichTextEditor", control_family="classic")
class RichTextEditorControl(BaseControl):
    def get_control_name(self):
        return "Classic/RichTextEditor"

    def get_default_properties(self):
        return {
            # Key properties
            "Default": '"<p>Type here...</p>"',
            "HtmlText": '""',
            # Additional properties
            "AccessibleLabel": '"Rich text editor"',
            "DisplayMode": "DisplayMode.Edit",
            "EnableSpellCheck": True,
            "Height": 150,
            "TabIndex": 0,
            "Visible": True,
            "Width": 300,
            "X": 0,
            "Y": 0
        }
