from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))

messages = [SystemMessage(content= "You are a doctor"), HumanMessage(content= "Tell me about Diabetic Retinopathy")]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)