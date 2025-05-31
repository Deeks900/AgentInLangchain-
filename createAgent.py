from prompt import getPrompt
from llm import createllm
from tool import createTool
from langchain.agents import create_react_agent
from customTool import getWeatherData  # Assuming getWeatherData is defined in customTool.py

def createAgent():
    # Get the prompt
    prompt = getPrompt()
    
    agent = create_react_agent(
        llm=createllm,
        prompt=prompt,
        tools=[createTool(), getWeatherData],  # Assuming getWeatherData is defined in customTool.py
    )
    return agent
