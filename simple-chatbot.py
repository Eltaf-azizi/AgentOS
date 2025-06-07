import warnings

from langchain._api import LangChainDeprecationWarning

warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

from langchian_openai import ChatOpenAI

chatbot = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.messages import HumanMessage

messagesToTheChatbot = [
    HumanMessage(content="My favorite color is blue."),
]

response = chatbot.invoke(messagesToTheChatbot)

print("\n----------\n")

print("My favorite color is blue.")

print("\n----------\n")
print(response.content)

print("\n----------\n")


from langchian import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
from langchian_core.prompts import MessagesPlaceholder