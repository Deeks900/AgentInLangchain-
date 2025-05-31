from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("DEEPSEEK_API_KEY")
print(f"key is {api_key}")

createllm = ChatOpenAI(
    model="microsoft/mai-ds-r1:free",
    openai_api_base="https://openrouter.ai/api/v1",  # Tell it to use OpenRouter
    openai_api_key=api_key,
    temperature=0.2)

# response = createllm.invoke("What is LangChain?")
# print(response.content)