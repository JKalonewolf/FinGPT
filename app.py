import re
import speech_recognition as sr
import streamlit as st

from api_handler import get_rbi_updates, get_sebi_circulars, get_forex_rates
from faiss_indexer import FaissDocumentIndexer
from local_llama import ask_fingpt
from download_models import *

# --- Page Config ---
st.set_page_config(page_title="FinGPT: RBI & SEBI Legal Assistant", layout="wide")
st.title("📘 FinGPT: RBI & SEBI Legal Assistant")

# --- Sidebar Navigation ---
st.sidebar.header("Home")
navigation = st.sidebar.radio("Go to", ["Chat Assistant", "Document Search", "RBI & SEBI Updates", "Forex Rates"])

# --- Initialize Chat History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- File Uploader for PDFs ---
st.sidebar.header("📂 Document Upload")
uploaded_files = st.sidebar.file_uploader("Upload RBI/SEBI PDF files", type=["pdf"], accept_multiple_files=True)

# Save uploaded PDFs to a folder
upload_dir = "uploaded_pdfs"
os.makedirs(upload_dir, exist_ok=True)

for uploaded_file in uploaded_files:
    with open(os.path.join(upload_dir, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

# Reload indexer on every upload
indexer = FaissDocumentIndexer(pdf_folder=upload_dir)

# --- Navigation Logic ---
if navigation == "Chat Assistant":
    st.header("💬 Chat with FinGPT")
    question = st.text_input("Ask something (RBI/SEBI):", key="chat_input")

    if st.button("Send"):
        if question.strip():
            with st.spinner("Thinking..."):
                context = "\n".join(
                    [f"Q: {e['question']}\nA: {e['answer']}" for e in st.session_state.chat_history[-3:]])
                full_prompt = f"{context}\nQ: {question}\nA:"
                answer = ask_fingpt(full_prompt, indexer=indexer)

            # Save to history
            st.session_state.chat_history.append({"question": question, "answer": answer})
            st.experimental_rerun()

    # Display Chat History
    if st.session_state.chat_history:
        st.write("### 📜 Conversation History")
        for entry in st.session_state.chat_history[::-1]:
            st.markdown(f"**You:** {entry['question']}")
            st.markdown(f"🧠 **FinGPT:** {entry['answer']}")
            st.divider()

elif navigation == "Document Search":
    st.header("🔎 Search Inside Documents")
    search_query = st.text_input("Enter search query:")

    # Highlight the search term inside the paragraph
    def highlight_text(text, term):
        highlighted = re.sub(f"(?i)({term})", r"**\1**", text)
        return highlighted

    if st.button("Search Documents"):
        with st.spinner("Searching..."):
            results = indexer.search(search_query, top_k=3)
            if results:
                for filename, paragraph in results:
                    st.markdown(f"**📄 Document:** `{filename}`")
                    st.markdown(highlight_text(paragraph, search_query))
                    st.divider()
            else:
                st.info("No matches found in the uploaded documents.")

elif navigation == "RBI & SEBI Updates":
    col1, col2 = st.columns(2)
    with col1:
        st.header("📈 Latest RBI Updates")
        rbi_updates = get_rbi_updates()
        if rbi_updates:
            for title, link in rbi_updates.items():
                st.markdown(f"- [{title}]({link})")
        else:
            st.info("No updates found.")

    with col2:
        st.header("📄 Latest SEBI Circulars")
        sebi_circulars = get_sebi_circulars()
        if sebi_circulars:
            for title, link in sebi_circulars.items():
                st.markdown(f"- [{title}]({link})")
        else:
            st.info("No circulars found.")

elif navigation == "Forex Rates":
    st.header("💰 Live Forex Rates")
    forex_rates = get_forex_rates()
    if forex_rates:
        for currency, rate in forex_rates.items():
            st.markdown(f"- **{currency}**: {rate}")
    else:
        st.info("Unable to fetch forex rates.")

# --- Voice Input Section ---
st.sidebar.header("🎙 Voice Input")
if st.sidebar.button("🎤 Speak your question"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.sidebar.info("Listening... Please speak now.")
        audio = recognizer.listen(source, timeout=5)

    try:
        voice_text = recognizer.recognize_google(audio)
        st.sidebar.success(f"🗣 You said: {voice_text}")
        question = voice_text
        st.experimental_rerun()
    except sr.UnknownValueError:
        st.sidebar.warning("Could not understand the audio.")
    except sr.RequestError:
        st.sidebar.error("Could not connect to speech recognition service.")
