from helper.llm_helpers import get_prompt_response

zero_shot_cot = f"""
    Q: A shop sells pens at $3 each. I buy 7 pens and pay with a $50 bill.
    How much change do I get?

    Let's think step by step.
"""

few_shot_cot = f"""
    Q: Roger has 5 balls. He buys 2 cans of 3 balls each. How many balls now?
    A: He starts with 5. 2 cans × 3 balls = 6 new balls. 5 + 6 = 11. Answer: 11

    Q: A cafe had 23 apples, used 20, then bought 6 more. How many apples?
    A:
"""

# Separate the reasoning from the answer
structured_cot = f"""
    Solve the problem. Put your reasoning in <thinking> tags
    and the final result alone in <answer> tags.

    Problem: A train leaves at 2:15 PM and the trip takes 3h 50m. When does it arrive?
"""

# Self consistency example
self_consistency_instruction = """Imagine three completely independent experts who
reason differently are answering this question. The final answer is obtained by
majority vote. The question is: """

problem_to_solve = """If there are 10 cars in the parking lot and 3 more cars arrive.
Half the original number of cars leave. Then, half of the current number of cars
arrive. How many cars are there in the parking?"""

self_consistency_prompt = self_consistency_instruction + problem_to_solve

print(f"Zero Shot Chain of Thought: \n{get_prompt_response(zero_shot_cot)}")

print(f"\nFew Shot Chain of Thought: \n{get_prompt_response(few_shot_cot)}")

print(f"\nStructured Chain of Thought: \n{get_prompt_response(structured_cot)}")

print(f"\Chain of Thought with Self Consistency: \n{get_prompt_response(self_consistency_prompt)}")