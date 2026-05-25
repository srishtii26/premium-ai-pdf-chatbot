import streamlit as st
import pandas as pd

def show_dashboard(
    uploaded_files,
    docs,
    messages
):

    st.title("📊 Analytics Dashboard")

    pdf_count = len(uploaded_files)

    page_count = len(docs)

    message_count = len(messages)

    data = {
        "Metric": [
            "PDFs",
            "Pages",
            "Messages"
        ],
        "Count": [
            pdf_count,
            page_count,
            message_count
        ]
    }

    df = pd.DataFrame(data)

    st.bar_chart(
        df.set_index("Metric")
    )

    st.dataframe(df)