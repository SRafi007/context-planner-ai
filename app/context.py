from dataclasses import dataclass, field
from typing import Callable, Any, Dict
import json
from pathlib import Path
import subprocess

CONTEXT_FILE = Path("data/context.json")


@dataclass
class Context:
    context: Dict[str, Any] = field(default_factory=dict)
    llm: Callable[[str], str] = None

    def load(self):
        if CONTEXT_FILE.exists():
            with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
                self.context = json.load(f)

        else:
            self.context = {}

    def save(self):
        with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
            json.dump(self.context, f, indent=2)


# --- Global shared context instance ---
ctx = Context()


# --- LLM using Ollama ---
def init_llm(model_name="mistral"):
    def run_llm(prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", model_name],
            input=prompt.encode(),
            capture_output=True,
        )
        return result.stdout.decode().strip()

    ctx.llm = run_llm
    ctx.load()
