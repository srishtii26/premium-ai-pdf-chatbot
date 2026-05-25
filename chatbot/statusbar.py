import streamlit as st

def show_statusbar(
    uploaded_files,
    model_name
):

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success("🟢 AI Online")

    with col2:

        st.info(
            f"🤖 Model: {model_name}"
        )

    with col3:

        pdf_count = len(uploaded_files)

        st.warning(
            f"📄 PDFs: {pdf_count}"
        )