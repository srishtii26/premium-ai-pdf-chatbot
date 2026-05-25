import streamlit as st
import time

def show_thinking():

    thinking_box = st.empty()

    messages = [
        "🧠 Analyzing documents...",
        "📄 Retrieving relevant information...",
        "⚡ Generating AI response...",
        "🚀 Preparing final answer..."
    ]

    for msg in messages:

        thinking_box.info(msg)

        time.sleep(0.6)

    thinking_box.empty()