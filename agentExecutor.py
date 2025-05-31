from langchain.agents import AgentExecutor
from createAgent import createAgent
from tool import createTool
from customTool import getWeatherData  

def createAgentExecutor():
    # Create the agent
    agent = createAgent()
    
    # Create the tool
    tool1 = createTool()
    tool2 = getWeatherData
    
    # Create the AgentExecutor with the agent and tool
    agent_executor = AgentExecutor(agent=agent, tools=[tool1, tool2], verbose=True,handle_parsing_errors=True)
    
    return agent_executor

response = createAgentExecutor().invoke({"input":"What is the capital of India and what is the weather there?"})
print(response['output'])