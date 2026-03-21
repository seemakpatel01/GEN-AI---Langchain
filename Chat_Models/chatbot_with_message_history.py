from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model = "llama-3.1-8b-instant")


messages =[
    SystemMessage(content = "you are a helpful assistant.")
]

while True:
    user_input = input('User: ')
    messages.append(HumanMessage(content = user_input))
    if user_input == "exit":
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content = result.content))
    print("AI: ", result.content)
    
print(messages)
    
