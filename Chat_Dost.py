import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv(override=True)

# Set up Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Configure Streamlit UI
st.set_page_config(page_title="Chat-Dost App", layout="centered")
st.title("🤖Chat-Dost")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Reset button
if st.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.success("Chat history cleared.")

# User input
user_input = st.text_input("Ask something:", key="input")

# If user types and clicks send
if st.button("Send") and user_input:
    # Add user message
    st.session_state.chat_history.append(user_input)

    with st.spinner("Dost is thinking..."):
        # Get response from Gemini
        response = model.invoke(st.session_state.chat_history)

    # Add response to chat history
    st.session_state.chat_history.append(response.content)

# Display conversation
if st.session_state.chat_history:
    st.markdown("### 💬 Chat History")
    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 Dost:** {msg}")
