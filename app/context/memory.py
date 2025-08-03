import json
import os
from datetime import datetime
from typing import List, Dict

SHORT_TERM_FILE = "data/short_term_memory.json"
LONG_TERM_FILE = "data/long_term_memory.json"


# ----------short memory
def load_short_term_memory(limit: int = 10) -> List[Dict]:
    if not os.path.exists(SHORT_TERM_FILE):
        return []

    with open(SHORT_TERM_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
    return memory[-limit:]  # Only return the most recent entries


def save_to_short_term_memory(entry: dict):
    memory = load_short_term_memory(limit=1000)  # Load more for saving

    entry["timestamp"] = datetime.now().isoformat()
    memory.append(entry)
    with open(SHORT_TERM_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)


# ---------=long memory


def long_term_memory() -> List[Dict]:
    if not os.path.exists(LONG_TERM_FILE):
        return []
    with open(LONG_TERM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def add_to_long_term_memory(summary: str, tags: List[str]):
    memory = long_term_memory()
    memory.append({"summary": summary, "tags": tags})
    with open(LONG_TERM_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)


def query_long_term_memory(Keywords: List[str]) -> List[str]:

    memory = long_term_memory()

    matches = [
        m["summary"]
        for m in memory
        if any(tag in Keywords for tag in m.get("tags", []))
    ]
    return matches


# -----summarize rexent memory


def summarize_short_term_memory() -> str:
    """Stub for now – later we’ll use LLM summarization."""
    recent = load_short_term_memory(limit=5)
    summaries = [f"{item['input']} -> {item.get('intent')}" for item in recent]
    return " | ".join(summaries)
