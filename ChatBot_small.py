from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Force reload .env values

# # Check which key is now being used
# print("API Key in use:", os.getenv("GOOGLE_API_KEY"))

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))

chat_history = []

def get_response(user_input):
    chat_history.append(user_input)
    response = model.invoke(chat_history)
    chat_history.append(response.text)
    return response.text

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = get_response(user_input)
    print(response)