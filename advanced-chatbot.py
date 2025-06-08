import warnings
from langchain._api import LangChainDeprecationWarning

warning.simplefilter("ignore", category=LangChainDeprecationWarning)

import os 

from dotenv import load_dotenv, find_dotenv
from langchain_core.messages import HumanMessage

messagesToTheChatbot = [
    HumanMessage(content="My favorite color is blue.")
]