from controls.base import BaseControl
from control_factory import register_control

@register_control("BarcodeReader", control_family="classic")
class BarcodeReaderControl(BaseControl):
    def get_control_name(self):
        return "BarcodeReader"

    def get_default_properties(self):
        return {
            "Text": "\"Scan Barcode\"",
            "BarcodeType": "Auto",
            "ScanningMode": "Automatic",
            "ScanningQuality": "Automatic",
            "PreferFrontCamera": False,
            "BeepOnScan": True,
            "VibrateOnScan": True,
            "OnScan": "",
            "OnCancel": "",
            "OnChange": "",
            "BorderColor": "=ColorFade(Self.Fill, -15%)",
            "BorderStyle": "BorderStyle.Solid",
            "BorderThickness": 1,
            "DisplayMode": "DisplayMode.Edit",
            "Height": 40,
            "Tooltip": "\"Scan a barcode\"",
            "Visible": True,
            "Width": 200,
            "X": 0,
            "Y": 0
        }
