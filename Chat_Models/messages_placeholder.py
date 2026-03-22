from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

chat_template = ChatPromptTemplate([
    ("system" , "You are a helpful customer suuport agent"), 
    MessagesPlaceholder(variable_name =  "chat_history"),
    ("human" , '{query}')  
])

chat_history = []

with open ('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
#print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'my refund?'})
print(prompt)
#chat_template.invoke
    








 