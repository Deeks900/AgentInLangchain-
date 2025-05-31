from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
import requests

def createTool():
    #Using a implicit tool in LangChain
    searchTool = DuckDuckGoSearchResults()
    #These tools are also runnables 
    # result=searchTool.invoke("What is LangChain?")
    # print(result)
    return searchTool