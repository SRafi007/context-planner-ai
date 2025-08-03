import json
from pathlib import Path

MEMORY_FILE = Path("data/user_memory.json")


def load_memory() -> dict:

    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    return {}


def save_memory(data: dict):
    MEMORY_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def update_memory(key: str, value):
    data = load_memory()
    data[key] == value
    save_memory(data)


def get_memory(key: str, default=None):
    return load_memory().get(key, default)
