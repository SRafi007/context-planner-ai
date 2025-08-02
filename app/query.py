from app.task_manager import load_tasks
import re


def search_tasks(query: str) -> str:
    tasks = load_tasks()
    query_lower = query.lower()

    matches = []
    for t in tasks:
        text = f"{t.get('title', '')} {t.get('date', '')} {t.get('time', '')} {' '.join(t.get('participants', []))}".lower()
        if re.search(query_lower, text):
            matches.append(t)

    if not matches:
        return "NO matching tasks found"

    return "\n".join(
        f"- {t.get('title')} on {t.get('date')} at {t.get('time', 'TBD')} with {', '.join(t.get('participants', [])) or 'N/A'}"
        for t in matches
    )
