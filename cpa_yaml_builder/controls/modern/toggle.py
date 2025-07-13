from cpa_yaml_builder.controls.base import BaseControl
from cpa_yaml_builder.control_factory import register_control

@register_control("toggle", control_family="modern")
class ToggleControl(BaseControl):
    def get_control_name(self):
        return "Toggle"

    def get_default_properties(self):
        return {
            "Label": '"Toggle Label"',
            "AccessibilityLabel": '"Toggle Accessibility Label"',
            "Visible": True,
            "Checked": False,
            "DisplayMode": 'DisplayMode.Edit',
            "LabelPosition": '"Left"',
            "X": 0,
            "Y": 0,
            "Width": 100,
            "Height": 40,
            "BasePaletteColor": '"ThemePrimary"',
            "Font": '"Segoe UI"',
            "FontSize": 14,
            "FontColor": '"#000000"',
            "FontWeight": '"Normal"',
            "FontItalic": False,
            "FontUnderline": False,
            "FontStrikethrough": False,
            "OnCheck": 'Notify("Toggle checked", NotificationType.Information)',
            "OnUncheck": 'Notify("Toggle unchecked", NotificationType.Information)',
            "OnSelect": 'Notify("Toggle selected", NotificationType.Information)',
            }
