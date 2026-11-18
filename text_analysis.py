from helper.llm_helpers import get_prompt_response

prompt = f"""
    Analyze the customer review below. Return only valid JSON with these fields:

    - "sentiment": positive, negative, neutral, or mixed
    - "confidence": a number from 0 to 1
    - "topics": a list of the main subjects mentioned
    - "emotions": a list of emotions expressed
    - "key_complaints": a list (empty if none)
    - "one_line_reason": a short justification for the sentiment

    Review:
    "The camera quality is stunning and the battery lasts all day. But the app keeps crashing, and support took a week to reply. I'm torn about keeping it."
"""

print(get_prompt_response(prompt))