import streamlit as st

def show_suggestions():

    st.subheader("💡 Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "📄 Summarize this document"
        )

        st.info(
            "🧠 What are the main topics?"
        )

    with col2:

        st.info(
            "📌 Explain key concepts"
        )

        st.info(
            "⚡ Give important insights"
        )