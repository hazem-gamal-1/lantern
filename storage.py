import json


def load():
    try:
        with open("tasks.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)