import json
import os

def write_json(filename):
    data = {
        "people": [
            {"name": "John doe", "age": 30},
            {"name": "jane Smith", "age": 25}
        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print(f"Wrote{filename} successful")