from .loader import load_data


def generate_diff(file1: str, file2: str):
    data1 = load_data(file1)
    data2 = load_data(file2)
    diff = sort_keys(data1, data2)
    result = []
    for key, info in sorted(diff.items(), key=lambda x: x[0]):
        action, *values = info
        values = [val if not isinstance(val, bool) else str(val).lower() for val in values]
        match action:
            case "kept":
                result.append(f"    {key}: {values[0]}")
            case "changed":
                result.append(f"  - {key}: {values[0]}")
                result.append(f"  + {key}: {values[1]}")
            case "added":
                result.append(f"  + {key}: {values[0]}")
            case "deleted":
                result.append(f"  - {key}: {values[0]}")
    return "{\n" + "\n".join(result) + "\n}"


def sort_keys(old: dict, new: dict) -> dict:
    all_keys = list(old.keys() | new.keys())
    common_keys = list(old.keys() & new.keys())
    result = {}
    for key in all_keys:
        if key in common_keys:
            value = ("kept", old[key]) if old[key] == new[key] else ("changed", old[key], new[key])
        else:
            value = ("deleted", old[key]) if key in old.keys() else ("added", new[key])
        result.update({key: value})
    return result
