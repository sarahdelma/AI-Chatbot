import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("🧠 Local AI Chatbot – Data Q&A")

uploaded_file = st.file_uploader("Upload your CSV or JSON", type=["csv", "json"])
if uploaded_file:
    with st.spinner("Uploading..."):
        res = requests.post(f"{BACKEND_URL}/upload", files={"file": uploaded_file})
        if res.status_code == 200:
            st.session_state["file_path"] = res.json()["path"]
            st.success("File uploaded successfully!")

if "file_path" in st.session_state:
    st.write(f"📁 Using file: {st.session_state['file_path']}")
    question = st.text_input("Ask a question about your data:")
    if st.button("Ask"):
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{BACKEND_URL}/ask",
                params={"file_path": st.session_state["file_path"], "question": question},
            )
            if res.status_code == 200:
                st.write("💬 **Answer:**")
                st.info(res.json()["answer"])
