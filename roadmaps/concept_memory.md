 Memory Design Overview
📂 Files:
data/short_term_memory.json → recent context (limited window)

data/long_term_memory.json → compressed knowledge (acts as a KB)

🏗️ Step 1: Memory Storage Format
Example: short_term_memory.json
json
Copy code
[
  {
    "timestamp": "2025-08-03T18:42:00",
    "input": "schedule a meeting with Rafi tomorrow at 4 PM",
    "intent": "add_task",
    "entities": {
      "task": "meeting with Rafi",
      "date": "2025-08-04",
      "time": "16:00"
    }
  }
]
Example: long_term_memory.json
json
Copy code
[
  {
    "summary": "User often schedules meetings with Rafi in the afternoon.",
    "tags": ["meeting", "Rafi", "pattern"]
  },
  {
    "summary": "Preferred meeting time is between 3–5 PM.",
    "tags": ["time_preference"]
  }
]