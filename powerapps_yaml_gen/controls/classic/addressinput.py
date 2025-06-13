from controls.base import BaseControl
from control_factory import register_control

@register_control("AddressInput", control_family="classic")
class AddressInputControl(BaseControl):
    def get_control_name(self):
        return "AddressInput"

    def get_default_properties(self):
        return {
            "BorderColor": "=ColorFade(Self.FillColor, -15%)",
            "BorderRadius": 2,
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "ContentLanguage": "=Language()",
            "CountrySet": "\"US,CA,MX\"",
            "Default": "\"\"",
            "DisabledBorderColor": "=RGBA(166, 166, 166, 1)",
            "DisabledFillColor": "=RGBA(240, 240, 240, 1)",
            "DisabledFontColor": "=RGBA(166, 166, 166, 1)",
            "DisplayMode": "DisplayMode.Edit",
            "FillColor": "=RGBA(255, 255, 255, 1)",
            "Font": "=Font.'Open Sans'",
            "FontSize": 14,
            "FontWeight": "FontWeight.Normal",
            "Height": 40,
            "HintText": "\"Enter address\"",
            "HoverBorderColor": "=ColorFade(Self.BorderColor, 20%)",
            "HoverFillColor": "=ColorFade(RGBA(255, 255, 255, 1), -20%)",
            "HoverFontColor": "=RGBA(0, 0, 0, 1)",
            "Italic": False,
            "Language": "=Language()",
            "Latitude": 0.0,
            "LineHeight": 1.2,
            "Longitude": 0.0,
            "OnAddressSelect": False,
            "OnChange": False,
            "PaddingBottom": 5,
            "PaddingLeft": 10,
            "PaddingRight": 10,
            "PaddingTop": 5,
            "PressedBorderColor": "=Self.BorderColor",
            "PressedFillColor": "=Self.FillColor",
            "PressedFontColor": "=Self.TextColor",
            "Radius": 0.0,
            "SearchResultLimit": 5,
            "SearchWithinRadius": False,
            "Strikethrough": False,
            "TabIndex": 0,
            "TextAlignment": "Align.Left",
            "TextColor": "=RGBA(0, 0, 0, 1)",
            "Tooltip": "\"Enter address\"",
            "Underline": False,
            "Visible": True,
            "Width": 300,
            "X": 0,
            "Y": 0
        }
