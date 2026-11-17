import os
from dotenv import load_dotenv
from helper.llm_helpers import get_response

load_dotenv()

api_key = os.getenv("API_KEY")
ai_model = os.getenv("AI_MODEL")

messages = [
    {
        "role": "user",
        "content": """
            Q: Sum the numbers 3, 5, and 6. A: 3+5+6=14
            Q: Sum the numbers 2, 4, and 7. A:
        """
    }
]

response1 = get_response(ai_model, 0, 150, messages)
response2 = get_response(ai_model, 0, 150, [
    {
        "role": "user",
        "content": """
            Review: "The battery on this phone dies too fast."
            Output: {"product": "phone", "sentiment": "negative"}

            Review: "Love my new headphones, great sound!"
            Output:
            
            Review: "This computer is too slow!"
            Output: 
        """
    }
])

print(f"Response 1 {response1}")
print(f"Response 2 {response2}")