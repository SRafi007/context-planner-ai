# MCP context handler — loads, updates, saves context.

import json
import os

CONTEXT_FILE = os.path.join("data", "context.json")


class MCPContext:
    def __init__(self):
        self.context = self.load_context()

    def load_context(self):
        if not os.path.exists(CONTEXT_FILE):
            return {}

        with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_context(self):
        with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
            json.dump(self.context, f, indent=2, ensure_ascii=False)

    def update(self, key, value):
        self.context[key] = value
        self.save_context()

    def get(self, key, default=None):
        return self.context.get(key, default)

    def reset(self):
        self.context = {}
        self.save_context()
