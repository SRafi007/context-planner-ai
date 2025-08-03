# app/executor
from app.core.task_manager import (
    add_task,
    list_all_tasks,
    cancel_task_by_title,
    find_task_conflicts,
)
from app.context.memory import save_to_short_term_memory, add_to_long_term_memory
from app.core.planner import find_task_conflicts


def handle_intent(context: dict) -> str:
    intent = context.get("current_intent")
    entities = context.get("entities", {})

    # Save to short-term memory
    save_to_short_term_memory(
        {
            "input": context.get("raw_input", "N/A"),
            "intent": intent,
            "entities": entities,
        }
    )

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

    # ✅ Fix typo from LLM or parser
    if "tiem" in entities and "time" not in entities:
        entities["time"] = entities.pop("tiem")

    task = {
        "title": entities.get("task", "Untitled task"),
        "date": entities.get("date", "unspecified"),
        "time": entities.get("time", "unspecified"),
        "participants": entities.get("participants", []),
    }

    # Conflict check
    conflicts = find_task_conflicts(task["date"], task["time"])
    if conflicts:
        return (
            f"⚠️ Conflict detected with {len(conflicts)} existing task(s):\n"
            + "\n".join(f"- {c['title']} at {c['time']}" for c in conflicts)
        )

    add_task(task)
    return f"Task '{task['title']}' added on {task['date']} at {task['time']}."


def execute_intent(context: dict) -> str:  # NEW
    """Public wrapper for compatibility with API."""
    return handle_intent(context)
