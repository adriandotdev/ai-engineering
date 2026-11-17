import os
from openai import OpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client = OpenAI(
    base_url='https://openrouter.ai/api/v1',
    api_key=api_key
)

"""
NOTE: list[...] only woks on Python 3.9 onwards version
"""
class Conversation(TypedDict):
    role: str
    content: str
    
def get_response(model: str, temperature: float, max_tokens: int, messages: list[Conversation]):
    response = client.chat.completions.create(
        model = model,
        temperature = temperature,
        max_completion_tokens = max_tokens,
        messages = messages
    )
    return response.choices[0].message.content