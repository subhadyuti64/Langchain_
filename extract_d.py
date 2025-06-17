from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

text = "I am Subhadyuti Rath. I am really ill and I want to book an appointment for my eye checkup with Dr.Ramesh Chandra. Can you please book an appointment for me with him on 22 June,2025 at 8pm"

prompt = PromptTemplate(
    template = """Extract the following information from the following text: {text}
    The informations are Patient Name, Doctor Name, Time of Appointment, Date of Appointment. Give the output in dictionary format""",
    input_variables = ["text"]
)

chain = prompt | model

res = chain.invoke({'text':text})

print(res.content)