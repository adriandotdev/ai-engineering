from helper.llm_helpers import get_prompt_response

prompt = f"""
  Compose a travel blog as follows:
    Step 1: Introduce the destination.
    Step 2: Share personal adventures during the trip.
    Step 3: Summarize the journey.  
"""

response = get_prompt_response(prompt)

print(f"Blog: {response}")