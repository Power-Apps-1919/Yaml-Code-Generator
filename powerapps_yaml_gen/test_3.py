from powerapps_yaml_gen.controls.classic.button import ButtonControl

def test_button_control():
    control = ButtonControl("TestButton", {})
    control_name, prop_keys = control.get_control_and_property_keys()
    print("Control name:", control_name)
    print("Property keys:", prop_keys)
    print(control.get_control_and_property_keys())
if __name__ == "__main__":
    test_button_control()