import streamlit as st

def show_followups():

    st.markdown("### 💡 Suggested Follow-ups")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "📘 Explain this simply"
        )

        st.info(
            "🧠 Give examples"
        )

    with col2:

        st.info(
            "📌 Key takeaways"
        )

        st.info(
            "⚡ Summarize this topic"
        )