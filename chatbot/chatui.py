import streamlit as st

def user_message(message):

    st.markdown(f"""
    <div style="
        background:#4F46E5;
        padding:14px;
        border-radius:18px;
        margin-bottom:10px;
        color:white;
        text-align:right;
    ">
    👤 {message}
    </div>
    """, unsafe_allow_html=True)

def assistant_message(message):

    st.markdown(f"""
    <div style="
        background:#1F2937;
        padding:14px;
        border-radius:18px;
        margin-bottom:14px;
        color:white;
    ">
    🤖 {message}
    </div>
    """, unsafe_allow_html=True)