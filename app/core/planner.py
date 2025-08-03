# Basic intent and entity detection logic.
import re
from utils.date_parser import parse_natural_date, normalize_time


def find_task_conflicts(date: str, time: str) -> list:
    from app.core.task_manager import load_tasks

    tasks = load_tasks()

    norm_time = normalize_time(time)
    conflicts = []

    for task in tasks:
        if task.get("date") == date and normalize_time(task.get("time")) == norm_time:
            conflicts.append(task)
    return conflicts


def detect_intent_and_entities(user_input: str):
    user_input = user_input.lower()
    intent = "unknown"
    entities = {}

    # intent_detection

    if any(word in user_input for word in ["add", "schedule", "create", "set up"]):
        intent = "add_task"

    # extract_date and time

    date = parse_natural_date(user_input)

    if date:
        entities["date"] = date

    # extract time

    time_match = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\b", user_input)
    if time_match:
        hour = int(time_match.group(1))
        minute = int(time_match.group(2) or "0")
        meridian = time_match.group(3)

        if meridian == "pm" and hour < 12:
            hour += 12
        time_str = f"{hour:02d}:{minute:02d}"
        entities["tiem"] = time_str

    # extract des (after , add, schedule)

    des_match = re.search(r"(?:add|schedule|create|set up)\s+(.*)", user_input)
    if des_match:
        entities["task"] = des_match.group(1)

    return intent, entities
