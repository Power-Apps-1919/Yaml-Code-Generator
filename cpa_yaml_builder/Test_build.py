# test_label.py
from builder import build_control_yaml

yaml_output1 = build_control_yaml(
    control_type="Button",
    name="btnSubmit",
    props={"Text": '"Submit"', "X": 100, "Y": 200},
    control_family="Classic"
)
print(yaml_output1)
