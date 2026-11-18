from helper.llm_helpers import get_prompt_response

prompt = """
    Transform the text below in three ways:

    1. Rewrite it in a formal business tone.
    2. Rewrite it in a casual, friendly tone.
    3. Convert it into a JSON object with the keys "sender", "issue", and "requested_action".

    Keep the meaning the same in every version.

    Text:
    "hey, so the printer on floor 3 keeps jamming and it's been like that since monday. can someone from IT come fix it asap? thx - Maria"
"""

prompt2 = """

    Transform the text below in four ways:

    1. Formal business tone.
    2. Casual, friendly tone.
    3. A JSON object with the keys "sender", "issue", "requested_action", and "urgency" (low, medium, or high).
    4. A single tweet-length version (under 200 characters).

    Keep the meaning the same in every version.

    Text:
    "hey team, the wifi in the east wing has been dropping every afternoon since last week and it's killing our video calls. also the coffee machine is broken lol. can facilities look at the wifi first? it's pretty urgent for us. - Jon"
"""

print(get_prompt_response(prompt))
print(f"\n{get_prompt_response(prompt2)}")