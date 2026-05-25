import streamlit as st

def show_logo():

    st.sidebar.image(
        "assets/images/logo.png",
        width=120
    )

    st.sidebar.markdown("""
    <h2 style='text-align:center;'>
    NovaMind AI
    </h2>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <p style='text-align:center;
    color:gray;'>
    AI Knowledge Platform
    </p>
    """, unsafe_allow_html=True)

    st.sidebar.divider()