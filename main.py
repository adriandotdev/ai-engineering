from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
ai_model = os.getenv("AI_MODEL")

client = OpenAI(
    base_url='https://openrouter.ai/api/v1',
    api_key=api_key,
)

model = ai_model
messages = [
    {
        "role": "system",
        "content": "You are a Hunger Games expert. If you ask a topic that it is not Hunger Games related please reply -> I only know Hunger Games topic."
    }
]

messages.append({
    "role": "user",
    "content": "Who is Katniss Everdeen?"
})

responses = client.chat.completions.create(
    model=model, 
    messages=messages, 
    reasoning_effort="medium"
)

print(responses.choices[0].message.content)