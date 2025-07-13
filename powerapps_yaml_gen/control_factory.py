import importlib
import pkgutil
from typing import Dict, Type
from controls.base import BaseControl

# Registry for all control types
CONTROL_REGISTRY: Dict[str, Dict[str, Type[BaseControl]]] = {
    "classic": {},
    "modern": {},
}

def register_control(control_type: str, control_family: str = "classic"):
    """
    Decorator to register a control class.
    """
    def decorator(cls):
        CONTROL_REGISTRY.setdefault(control_family, {})[control_type] = cls
        return cls
    return decorator

def auto_import_controls():
    """
    Auto-import all controls from the controls package.
    """
    import controls.classic
    import controls.modern

    for finder, name, ispkg in pkgutil.walk_packages(controls.__path__, controls.__name__ + "."):
        importlib.import_module(name)

def list_registered_controls(show_properties: bool = False):
    """
    Returns a list of all registered controls with their type and family.
    If show_properties is True, also includes the default properties for each control.
    """
    result = []
    for family, controls in CONTROL_REGISTRY.items():
        for control_type, control_cls in controls.items():
            entry = {"type": control_type, "family": family}
            if show_properties:
                try:
                    # Create a dummy instance to get default properties
                    instance = control_cls("Dummy", {})
                    entry["default_properties"] = instance.get_default_properties()
                except Exception as e:
                    entry["default_properties"] = f"Error: {e}"
            result.append(entry)
    return result

def create_control(control_type: str, name: str, props: dict, control_family: str = "classic") -> BaseControl:
    """
    Create an instance of a registered control class.
    """
    control_map = CONTROL_REGISTRY.get(control_family)
    if not control_map:
        raise ValueError(f"Unknown control family: {control_family}")

    control_cls = control_map.get(control_type)
    if not control_cls:
        raise ValueError(f"Unknown control type '{control_type}' in family '{control_family}'")

    return control_cls(name, props)
