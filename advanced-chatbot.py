import warnings
from langchain._api import LangChainDeprecationWarning

warning.simplefilter("ignore", category=LangChainDeprecationWarning)

import os 

from dotenv import load_dotenv, find_dotenv
from langchain_core.messages import HumanMessage

messagesToTheChatbot = [
    HumanMessage(content="My favorite color is blue.")
]

chatbot.invoke(messagesToTheChatbot)

chatbot.invoke([
    HumanMessage(content="What is my favorite color?")
])


from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory



chatbotMemory = {}

# input: session_id, output: chatbotMenory[session_id]
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in chatbotMemory:
        chatbotMemory[session_id] = ChatMessageHistory()
    return chatbotMemory[session_id]


chatbot_with_message_history = RunnableWithMessageHistory(
    chatbot,
    get_session_history
)

session1 = {"configurable": {"session_id": "001"}}


responseFromChatbot = chatbot_with_message_history.invoke(
    [HumanMessage(content="My favorite color is red.")],
    config=session1,
)

responseFromChatbot.content