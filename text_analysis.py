from helper.llm_helpers import get_prompt_response

prompt = """
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


prompt2 = """
    Analyze the review below. Return only valid JSON with these fields:
    "sentiment" (positive, negative, neutral, or mixed), "confidence" (0 to 1), "topics", "emotions", "key_complaints", "one_line_reason".

    Review:
    "Oh great, another update that totally fixed everything. Love how the app now crashes in half the time. Anyway, shipping was fast."
"""

print(get_prompt_response(prompt))

print(f"\n{get_prompt_response(prompt2)}")