# app/executor
from app.task_manager import add_task, list_all_tasks, cancel_task_by_title


def handle_intent(context: dict) -> str:
    intent = context.get("current_intent")

    if intent == "add_task":
        return handle_add_task(context)
    elif intent == "list_tasks":
        return list_all_tasks()
    elif intent == "cancel_task":
        task = context.get("entities", {}).get("task")
        if task:
            return cancel_task_by_title(task)
        else:
            return "I need the name of the task to cancel."
    else:
        return "I'm not sure how to handle that yet."


def handle_add_task(context: dict) -> str:
    entities = context.get("entities", {})
    task = {
        "title": entities.get("task", "Untitled task"),
        "date": entities.get("date", "unspecified"),
        "time": entities.get("time", "unspecified"),
        "participants": entities.get("participants", []),
    }
    add_task(task)
    return f"Task '{task['title']}' added on {task['date']} at {task['time']}."


def execute_intent(context: dict) -> str:  # NEW
    """Public wrapper for compatibility with API."""
    return handle_intent(context)
