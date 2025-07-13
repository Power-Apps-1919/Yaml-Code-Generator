from typing import Any

def format_value(val: Any) -> Any:
    """
    Prefixes every property value with '=' unless it's already a formula.
    Converts booleans and numbers to Power Fx expressions.
    """
    if isinstance(val, bool):
        return f"={'true' if val else 'false'}"
    if isinstance(val, (int, float)):
        return f"={val}"
    if isinstance(val, str):
        s = val.strip()
        return s if s.startswith('=') else f"={s}"
    return val

def ensure_serializable(data: Any) -> Any:
    """
    Recursively processes nested structures to apply formatting only to values,
    NOT keys. Keys and map structure remain untouched.
    """
    if isinstance(data, list):
        return [ensure_serializable(item) for item in data]
    elif isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                new_dict[key] = ensure_serializable(value)
            else:
                new_dict[key] = format_value(value)
        return new_dict
    else:
        return format_value(data)
