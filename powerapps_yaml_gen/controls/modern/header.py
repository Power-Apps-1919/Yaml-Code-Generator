from powerapps_yaml_gen.controls.base import BaseControl
from control_factory import register_control

@register_control("Header", control_family="modern")
class HeaderControl(BaseControl):
    def get_control_name(self):
        return "Modern/Header"

    def get_default_properties(self):
        return {
            # General
            "Title": '"Screen Title"',
            "IsTitleVisible": True,
            "Logo": '"https://example.com/logo.png"',
            "IsLogoVisible": True,
            "IsProfilePictureVisible": True,
            "Visible": True,
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 400,
            "Height": 56,
            # Style and theme
            "BasePaletteColor": '"ThemePrimary"',
            "Style": '"Brand"',
            "Font": '"Segoe UI"',
            "TitleFontSize": 20,
            "FontColor": '"#000000"',
            # Additional properties
            "DisplayMode": "DisplayMode.Edit",
            "LogoMaxHeight": 40,
            "LogoToolTip": '"App logo"',
            "OnSelectLogo": ""
        }
