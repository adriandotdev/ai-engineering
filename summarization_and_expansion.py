from helper.llm_helpers import get_prompt_response

prompt = f"""
    You will do two tasks on the text below.

    Task A (Summarize): Condense the text into exactly 2 sentences, keeping only the key facts.
    Task B (Expand): Rewrite the original text as a detailed paragraph of about 150 words. Add helpful context and examples, but do not invent facts.

    Text:
    "Remote work has changed how companies hire. Firms can now recruit from anywhere, which widens the talent pool, but they also compete with employers worldwide. Some managers report lower collaboration, while employees often report better focus and work-life balance."

    Output format:
    Summary: <2 sentences>
    Expanded: <~150 words>
"""

print(get_prompt_response(prompt))
