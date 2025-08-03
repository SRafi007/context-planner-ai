from app.memory import update_memory, get_memory


update_memory("last_meeting_with", "Sarah")
get_memory("last_meeting_with")  # → "Sarah"
