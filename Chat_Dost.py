import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.set_page_config(page_title="Chat-Dost App", layout="centered")
st.title("🤖Chat-Dost")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.success("Chat history cleared.")

user_input = st.text_input("Ask something:", key="input")

if st.button("Send") and user_input:
    st.session_state.chat_history.append(user_input)

    with st.spinner("Dost is thinking..."):
        response = model.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(response.content)


if st.session_state.chat_history:
    st.markdown("### 💬 Chat History")
    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 Dost:** {msg}")
