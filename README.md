# 🧠 Intelligent Daily Planner – Context-Aware Task Assistant

An intelligent planning assistant powered by local LLMs (via [Ollama](https://ollama.com)) that understands natural language and helps you:
- 📅 Schedule tasks and meetings
- 🔍 Search and summarize your day
- 💬 Maintain context-aware conversations
- ⚙️ Store memory and user preferences

---

## 🏗️ Project Structure

```
app/
├── __init__.py
├── core/             # 💡 Main logic & task processing
│   ├── planner.py
│   ├── task_manager.py
│   ├── executor.py
│   └── query.py
├── llm/              # 🧠 LLM-related processing
│   ├── llm_engine.py
│   ├── summarizer.py
│   ├── reply_engine.py  # (if you rename from main_cli)
│   └── prompts/
│       ├── base_prompt.txt
│       └── examples.md
├── context/          # 🧬 Context memory and parsing
│   ├── context.py
│   ├── context_manager.py
│   ├── memory.py
│   └── api.py
└── ui/               # 🎛️ Frontends
    ├── cli.py        # formerly main_cli.py
    └── streamlit_ui.py
```

---

## 🧪 Example Commands

```bash
> schedule a meeting with Sarah tomorrow at 4pm
✅ Reply: Meeting scheduled.
```

```bash
> summary
📋 You have a meeting tomorrow at 4 PM with Sarah.
```

```bash
> search "Sarah"
📌 Meeting with Sarah on 2025-07-30 at 4 PM
```

## 🛠 How to Run

### 1. Start Streamlit UI
```bash
streamlit run app/ui/streamlit_ui.py
```

### 2. Use CLI Interface (optional)
```bash
python -m app.ui.cli reply "schedule a meeting..."
```

## 🧠 LLM Backend

Uses Mistral 7B locally via Ollama for privacy-first offline reasoning.

## 🧩 Built With

- **Streamlit** – for frontend
- **Typer** – for CLI interface
- **Ollama** – local language model
- **Python 3.10+**

## 📌 TODO / Milestones

- [ ] Local LLM-powered intent understanding
- [ ] Streamlit + CLI frontends
- [ ] Auto memory recall for past tasks
- [ ] Calendar/notification integration
- [ ] Multi-user session handling