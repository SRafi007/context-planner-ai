from app.task_manager import load_tasks
from app.context import ctx


def generate_summary() -> str:
    tasks = load_tasks()
    if not tasks:
        return "You have no scheduled tasks."

    task_text = "\n".join(
        f"- {t.get('title')} on {t.get('date')} at {t.get('time', 'TBD')} with {', '.join(t.get('participants', [])) or 'N/A'}"
        for t in tasks
    )

    prompt = f"""Summarize the following user's schedule in a friendly, concise way:
{task_text}
Format the output like you're speaking to the user."""

    result = ctx.llm(prompt)
    return result
