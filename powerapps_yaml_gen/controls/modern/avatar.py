from controls.base import BaseControl
from control_factory import register_control

@register_control("Avatar", control_family="modern")
class AvatarControl(BaseControl):
    def get_control_name(self):
        return "Avatar"

    def get_default_properties(self):
        return {
            # Main properties
            "Name": "User().FullName",
            "Image": "User().Image",
            "Badge": '"Available"',
            "Visible": True,
            # Size and position
            "X": 0,
            "Y": 0,
            "Width": 48,
            "Height": 48,
            # Style and theme
            "Shape": '\'Avatar.Shape\'.Circular',
            "Appearance": '\'Avatar.Appearance\'.Brand',
            "BasePaletteColor": '"ThemePrimary"',
            "Font": '"Segoe UI"',
            "FontSize": 16,
            "FontColor": '"#000000"',
            "FontWeight": '"Normal"',
            "FontItalic": False,
            "FontUnderline": False,
            "FontStrikethrough": False,
            # Additional properties
            "OutOfOffice": False
        }
