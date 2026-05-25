import streamlit as st

def show_landing():

    st.markdown("""
    <h1 style='text-align:center;'>
    🚀 AI Knowledge Assistant
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align:center;
    font-size:18px;
    color:gray;'>
    Upload PDFs • Chat with Documents • Generate Insights
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📄 Multi PDF Upload")

    with col2:
        st.info("🤖 AI Powered Answers")

    with col3:
        st.info("⚡ Fast Local RAG")

    st.write("")