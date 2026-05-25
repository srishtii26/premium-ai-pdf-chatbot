import streamlit as st

def show_branding():

    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:20px;
        background:rgba(255,255,255,0.05);
        margin-bottom:20px;
    ">

    <h1 style="
        font-size:48px;
        margin-bottom:10px;
    ">
    🚀 NovaMind AI
    </h1>

    <p style="
        font-size:18px;
        color:gray;
    ">
    Intelligent Document Analysis Platform
    </p>

    </div>
    """, unsafe_allow_html=True)