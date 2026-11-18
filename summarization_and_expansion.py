from helper.llm_helpers import get_prompt_response

prompt = """
    You will do two tasks on the text below.

    Task A (Summarize): Condense the text into exactly 2 sentences, keeping only the key facts.
    Task B (Expand): Rewrite the original text as a detailed paragraph of about 150 words. Add helpful context and examples, but do not invent facts.

    Text:
    "Remote work has changed how companies hire. Firms can now recruit from anywhere, which widens the talent pool, but they also compete with employers worldwide. Some managers report lower collaboration, while employees often report better focus and work-life balance."

    Output format:
    Summary: <2 sentences>
    Expanded: <~150 words>
"""

prompt2 = """

    Task A (Summarize): Condense the text into exactly 1 sentence of at most 20 words.
    Task B (Expand): Rewrite the text as a paragraph of about 50 words. Do not invent facts.

    Text:
    "Remote work has changed how companies hire. Firms can now recruit from anywhere, which widens the talent pool, but they also compete with employers worldwide. Some managers report lower collaboration, while employees often report better focus and work-life balance."

    Output format:
    Summary: <1 sentence>
    Expanded: <~50 words>
"""

print(get_prompt_response(prompt))
print(f"\n{get_prompt_response(prompt2)}")
