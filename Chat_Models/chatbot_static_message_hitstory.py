from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(model = "llama-3.1-8b-instant",temperature = 0.9)

#chathistory list named as messages
messages = [
    SystemMessage(content = "You are a helpful assistant."),
    HumanMessage(content = "What is langchain?")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)




