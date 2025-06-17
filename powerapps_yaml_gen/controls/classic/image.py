from controls.base import BaseControl
from control_factory import register_control

@register_control("Image", control_family="classic")
class ImageControl(BaseControl):
    def get_control_name(self):
        return "Classic/Image"

    def get_default_properties(self):
        return {
            # Key property
            "Image": '"https://example.com/sample-image.png"',
            # Additional properties
            "AccessibleLabel": '"Image control"',
            "ApplyEXIFOrientation": True,
            "AutoDisableOnSelect": False,
            "BorderColor": "=RGBA(56, 96, 178, 1)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 0,
            "CalculateOriginalDimensions": False,
            "DisplayMode": "DisplayMode.Edit",
            "DisabledBorderColor": "=RGBA(166,166,166,1)",
            "DisabledFill": "=RGBA(244,244,244,1)",
            "Fill": "=RGBA(255,255,255,1)",
            "FlipHorizontal": False,
            "FlipVertical": False,
            "FocusedBorderColor": "=RGBA(0,120,212,1)",
            "FocusedBorderThickness": 2,
            "Height": 150,
            "HoverBorderColor": "=RGBA(0,120,212,1)",
            "HoverFill": "=RGBA(237,244,252,1)",
            "ImagePosition": "ImagePosition.Fit",
            "ImageRotation": "ImageRotation.None",
            "OnSelect": "",
            "OriginalHeight": 0,
            "OriginalWidth": 0,
            "PaddingBottom": 0,
            "PaddingLeft": 0,
            "PaddingRight": 0,
            "PaddingTop": 0,
            "PressedBorderColor": "=RGBA(0,96,178,1)",
            "PressedFill": "=RGBA(204,228,247,1)",
            "RadiusBottomLeft": 0,
            "RadiusBottomRight": 0,
            "RadiusTopLeft": 0,
            "RadiusTopRight": 0,
            "TabIndex": 0,
            "Tooltip": '"Image control tooltip"',
            "Transparency": 0,
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
