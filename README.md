# Prompt Engineering

A set of small Python scripts for practicing prompt engineering techniques. Each script sends one or more prompts to an LLM through [OpenRouter](https://openrouter.ai) (using the OpenAI Python SDK) and prints the responses.

## Techniques covered

| Script | What it demonstrates |
| --- | --- |
| [main.py](main.py) | A system prompt that restricts the model to one topic (Hunger Games) |
| [few_shot_prompt_and_one_shot_prompt.py](few_shot_prompt_and_one_shot_prompt.py) | One-shot and few-shot prompting (arithmetic and review sentiment extraction) |
| [multi_step_prompt.py](multi_step_prompt.py) | Multi-step prompting: a travel blog written in explicit steps |
| [chain_of_thought_prompt.py](chain_of_thought_prompt.py) | Zero-shot CoT, few-shot CoT, structured CoT (`<thinking>` / `<answer>` tags) and self-consistency |
| [virtual_paris_tourist_chatbot.py](virtual_paris_tourist_chatbot.py) | An interactive console chatbot (multi-turn, keeps conversation history) built from a layered system prompt (role, tone, guidelines, output format) |

Shared helpers live in [helper/llm_helpers.py](helper/llm_helpers.py):

- `get_response(model, temperature, max_tokens, messages)` sends a full message list with explicit settings.
- `get_prompt_response(prompt)` sends a single user prompt to the model set in `AI_MODEL`, with `reasoning_effort="low"`.

## Setup

Requires Python 3.9 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
```

Create a `.env` file in the project root (it is git-ignored):

```env
API_KEY=your-openrouter-api-key
AI_MODEL=provider/model-name
```

`AI_MODEL` is any model ID available on OpenRouter. Some scripts pass `reasoning_effort`, so pick a model that supports it.

## Running

Run each script from the project root so the `helper` package imports correctly:

```bash
python main.py
python few_shot_prompt_and_one_shot_prompt.py
python multi_step_prompt.py
python chain_of_thought_prompt.py
python virtual_paris_tourist_chatbot.py   # type "exit" to quit
```

## Notes

- Running these scripts makes real API calls and may incur costs.
- `virtual_paris_tourist_chatbot.py` reuses `get_response` from the helper module and calls the model set in `AI_MODEL`. Replies are capped at 150 tokens.
