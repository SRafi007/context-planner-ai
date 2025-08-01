import requests


def generate_reply(context: dict, user_input: str) -> str:
    prompt = f"""
You are a helpful assistant for managing tasks.

Here is the current context (JSON):
{context}

The user said: "{user_input}"

Respond clearly, ask follow-up if needed, and act based on the intent.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt.strip(), "stream": False},
    )

    return response.json()["response"].strip()
