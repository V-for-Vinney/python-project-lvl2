from pathlib import Path
import json

import yaml


def load_data(filename: str):
    ext = filename.split(".")[-1].lower()
    path = Path(filename)
    if ext == "json":
        data = json.load(open(path))
    elif ext in ["yaml", "yml"]:
        data = yaml.load(open(path), Loader=yaml.Loader)
    else:
        data = dict()
    return data
