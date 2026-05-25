import streamlit as st
import os
import time



from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

from streamlit_option_menu import option_menu

from chatbot.landing import show_landing
from chatbot.suggestions import show_suggestions
from chatbot.statusbar import show_statusbar
from chatbot.branding import show_branding
from chatbot.logo import show_logo
from chatbot.followups import show_followups
from chatbot.thinking import show_thinking
from chatbot.dashboard import show_dashboard
from chatbot.chatui import (
    user_message,
    assistant_message
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Premium AI PDF Chatbot",
    page_icon="📚",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()



# ---------------- BRANDING ---------------- #

show_branding()

show_landing()

# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:

    st.session_state.messages = []

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    show_logo()

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Chat",
            "Analytics"
        ],
        icons=[
            "chat",
            "bar-chart"
        ],
        default_index=0,
    )

    st.header("⚙️ Settings")

    model_name = st.selectbox(
        "Choose Model",
        ["tinyllama"]
    )

    chunk_size = st.slider(
        "Chunk Size",
        100,
        500,
        150
    )

    generate_summary = st.button(
        "📝 Generate Summary"
    )

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ---------------- FILE UPLOAD ---------------- #

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

# ---------------- DOCUMENT PROCESSING ---------------- #

documents = []
docs = []

if uploaded_files:

    for uploaded_file in uploaded_files:

        temp_path = uploaded_file.name

        with open(temp_path, "wb") as f:

            f.write(uploaded_file.read())

        loader = PyPDFLoader(temp_path)

        documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=20
    )

    docs = text_splitter.split_documents(documents)

# ---------------- ANALYTICS PAGE ---------------- #

if selected == "Analytics":

    if uploaded_files:

        show_dashboard(
            uploaded_files,
            docs,
            st.session_state.messages
        )

    else:

        st.warning("Upload PDFs first.")

# ---------------- CHAT PAGE ---------------- #

if selected == "Chat":

    show_statusbar(
        uploaded_files,
        model_name
    )

    show_suggestions()

    if uploaded_files:

        embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)

        vectorstore = FAISS.from_documents(
            docs,
            embeddings
        )

        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 1}
        )

        llm = OllamaLLM(
            model=model_name
        )

        # ---------------- SUMMARY ---------------- #

        if generate_summary:

            summary_context = "\n".join(
                [doc.page_content for doc in docs[:3]]
            )

            summary_prompt = f"""
            Create a short professional summary
            of these documents.

            Documents:
            {summary_context}
            """

            summary_response = llm.invoke(
                summary_prompt
            )

            st.subheader("📄 Document Summary")

            st.markdown(summary_response)

        # ---------------- CHAT HISTORY ---------------- #

        for message in st.session_state.messages:

            if message["role"] == "user":

                user_message(
                    message["content"]
                )

            else:

                assistant_message(
                    message["content"]
                )

        # ---------------- USER INPUT ---------------- #

        query = st.chat_input(
            "Ask a question from your PDFs..."
        )

        if query:

            show_thinking()

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": query
                }
            )

            user_message(query)

            retrieved_docs = retriever.invoke(query)

            context = "\n".join(
                [doc.page_content for doc in retrieved_docs]
            )

            prompt = f"""
            You are a helpful AI assistant.

            Answer ONLY from the provided context.

            If answer is unavailable,
            say:
            "I could not find this information."

            Context:
            {context}

            Question:
            {query}
            """

            response = llm.invoke(prompt)

            sources = []

            for doc in retrieved_docs:

                page = doc.metadata.get(
                    "page",
                    "Unknown"
                )

                sources.append(
                    f"Page {page + 1}"
                )

            source_text = "\n".join(
                list(set(sources))
            )

            final_response = f"""
{response}

---
📖 Sources:
{source_text}
"""

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": final_response
                }
            )

            assistant_message(final_response)

            show_followups()

    else:

        st.info("📄 Upload PDFs to start chatting.")

# ---------------- CLEANUP ---------------- #

if uploaded_files:

    for uploaded_file in uploaded_files:

        temp_path = uploaded_file.name

        if os.path.exists(temp_path):

            os.remove(temp_path)