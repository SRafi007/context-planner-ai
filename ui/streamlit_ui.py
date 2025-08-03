# ui/streamlit_ui.py

import sys
import os

# 👇 Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.context import ctx, init_llm
from app.llm_engine import generate_reply
from app.executor import handle_intent
from app.summarizer import generate_summary


st.set_page_config(page_title="Intelligent Daily Planner", layout="centered")

# --- Init LLM ---
init_llm("mistral")

st.title("🧠 Intelligent Daily Planner")

# --- USER COMMAND ---
user_input = st.text_input("What would you like to do?", key="command_input")

if st.button("Reply"):
    if user_input:
        reply = generate_reply(ctx.context, user_input)
        st.markdown(f"**LLM Response:** {reply}")
        st.json(ctx.context)
    else:
        st.warning("Please enter a command first.")

# --- EXECUTE INTENT ---
if st.button("Execute Intent"):
    result = handle_intent(ctx.context)
    st.success(f"✅ {result}")

# --- SUMMARY ---
if st.button("Daily Summary"):
    summary = generate_summary()
    st.info(summary)

# --- SEARCH ---
search_query = st.text_input("🔍 Search Tasks", key="search_input")
if st.button("Search"):
    if search_query:
        results = search_tasks(search_query)
        if results:
            for res in results:
                st.write(f"- {res}")
        else:
            st.warning("No tasks found.")
    else:
        st.warning("Please enter a search query.")
