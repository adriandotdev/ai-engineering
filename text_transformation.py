from helper.llm_helpers import get_prompt_response

prompt = f"""
    Transform the text below in three ways:

    1. Rewrite it in a formal business tone.
    2. Rewrite it in a casual, friendly tone.
    3. Convert it into a JSON object with the keys "sender", "issue", and "requested_action".

    Keep the meaning the same in every version.

    Text:
    "hey, so the printer on floor 3 keeps jamming and it's been like that since monday. can someone from IT come fix it asap? thx - Maria"
"""

print(get_prompt_response(prompt))
