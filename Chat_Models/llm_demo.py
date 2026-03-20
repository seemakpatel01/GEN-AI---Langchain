from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(    model="llama-3.1-8b-instant", temperature = 0.9, max_completion_tokens = 100)


result = llm.invoke("describe vibe of March? as a poem of 4 lines")
print(result.content)