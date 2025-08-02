import json
from pathlib import Path

TASK_FILE = Path("data/tasks.json")
TASK_FILE.parent.mkdir(parents=True, exist_ok=True)


def load_tasks():
    if TASK_FILE.exists():
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, intent=2)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)


def list_all_tasks():
    tasks = load_tasks()
    if not tasks:
        return "No task Scheduled"

    return "\n".join(
        f"- {t.get('title', 'Untitled')} on {t.get('date')} at {t.get('time', 'TBD')}"
        for t in tasks
    )


def cancel_task_by_title(title):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t.get("title") != title]
    if len(new_tasks) == len(tasks):
        return "No matching task found to cancel."

    save_tasks(new_tasks)
    return f"Cancelled task: {title}"
