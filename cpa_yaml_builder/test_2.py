import importlib
import pkgutil
from cpa_yaml_builder.controls.base import BaseControl

print("STARTING CONTROL DISCOVERY")
print(f"BaseControl in test script: {BaseControl}")

def get_all_controls_properties(package):
    controls_info = []

    def walk_modules(module):
        print(f"Scanning: {module.__name__}")
        for loader, name, is_pkg in pkgutil.iter_modules(module.__path__):
            full_name = f"{module.__name__}.{name}"
            print(f"  Found: {full_name}")
            try:
                submod = importlib.import_module(full_name)
                for attr in dir(submod):
                    obj = getattr(submod, attr)
                    if isinstance(obj, type):
                        print(f"    Class found: {obj.__name__} (module: {obj.__module__})")
                        try:
                            is_sub = issubclass(obj, BaseControl)
                        except Exception:
                            is_sub = False
                        print(f"      issubclass(obj, BaseControl): {is_sub}")
                    if isinstance(obj, type) and issubclass(obj, BaseControl) and obj is not BaseControl:
                        print(f"    Trying: {obj.__name__}")
                        try:
                            instance = obj("Dummy", {})
                            control_name = instance.get_control_name()
                            if 'classic' in full_name:
                                family = 'classic'
                            elif 'modern' in full_name:
                                family = 'modern'
                            else:
                                family = 'unknown'
                            controls_info.append((control_name, family))
                            print(f"      Added: {control_name} ({family})")
                        except Exception as e:
                            print(f"      Error: {e}")
                            continue
                if is_pkg:
                    walk_modules(submod)
            except Exception as e:
                print(f"    Import error: {e}")
                continue

    walk_modules(package)
    return controls_info


from cpa_yaml_builder.controls import classic, modern

classic_list = get_all_controls_properties(classic)
modern_list = get_all_controls_properties(modern)

print("Classic Controls:")
for name, family in classic_list:
    print(f"  {name} (family: {family})")
print("Modern Controls:")
for name, family in modern_list:
    print(f"  {name} (family: {family})")
print("DONE")