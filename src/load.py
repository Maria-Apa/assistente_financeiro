import json
import os

def load_json(filename):
    path = os.path.join("data", filename)
    return json.load(open(path, encoding="utf-8"))
