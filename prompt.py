from langsmith import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
# Get API key
api_key = os.getenv("LANGSMITH_API_KEY")

def getPrompt():
    client = Client(api_key=api_key)
    prompt = client.pull_prompt("hwchase17/react")
    return prompt    