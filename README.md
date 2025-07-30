### Project Name
# 📛 Name: context-planner-ai
### 📝 Description:

A modular AI-powered daily planner using Model Context Protocol (MCP) to manage tasks, schedules, and user intents through natural language. Built for learning and reuse in agent-based systems like JERVIS.
```
context-planner-ai/
│
├── app/                         # 🔧 Core application logic
│   ├── __init__.py
│   ├── main.py                  # Entry point (CLI or FastAPI)
│   ├── planner.py               # Intent handling & LLM orchestration
│   └── context_manager.py       # MCP context (load, update, serialize)
│
├── modules/                     # 🛠️ Pluggable tools (MCP-compatible)
│   ├── __init__.py
│   ├── task_tool.py             # Task creation, listing, completion
│   ├── calendar_tool.py         # Slot checking, date parsing
│   └── reminder_tool.py         # (Optional) Reminders and time alerts
│
├── prompts/                     # 🧠 LLM prompt templates
│   ├── base_prompt.txt          # Injects MCP context + task
│   └── examples.md              # Prompt patterns, use cases
│
├── data/                        # 📂 Runtime data (JSON/db)
│   ├── tasks.json               # Saved tasks
│   ├── user_profile.json        # User config, preferences
│   └── context.json             # MCP session state
│
├── tests/                       # ✅ Unit and integration tests
│   ├── test_context.py
│   ├── test_task_tool.py
│   └── test_calendar_tool.py
│
├── utils/                       # 🔧 Helper functions/utilities
│   ├── date_parser.py           # Natural language date handling
│   └── logger.py                # Logging and debugging
│
├── .env                         # 🔐 API keys (OpenAI, Calendar API, etc.)
├── .gitignore
├── README.md                    # 📘 Project overview
├── requirements.txt             # 🐍 Python dependencies
└── LICENSE                      # 📝 Open-source license
```