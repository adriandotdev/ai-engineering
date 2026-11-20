# AI Engineering

A hands-on repo for learning AI engineering: building applications on top of large language models (LLMs). It starts with prompt engineering, using small Python scripts to practice the core techniques. Each script sends one or more prompts to an LLM through [OpenRouter](https://openrouter.ai) (using the OpenAI Python SDK) and prints the responses. A second section runs open models locally with Hugging Face `transformers` pipelines.

## Prompt engineering techniques

| Script | What it demonstrates |
| --- | --- |
| [main.py](main.py) | A system prompt that restricts the model to one topic (Hunger Games) |
| [few_shot_prompt_and_one_shot_prompt.py](few_shot_prompt_and_one_shot_prompt.py) | One-shot and few-shot prompting (arithmetic and review sentiment extraction) |
| [multi_step_prompt.py](multi_step_prompt.py) | Multi-step prompting: a travel blog written in explicit steps |
| [chain_of_thought_prompt.py](chain_of_thought_prompt.py) | Zero-shot CoT, few-shot CoT, structured CoT (`<thinking>` / `<answer>` tags) and self-consistency |
| [virtual_paris_tourist_chatbot.py](virtual_paris_tourist_chatbot.py) | An interactive console chatbot (multi-turn, keeps conversation history) built from a layered system prompt (role, tone, guidelines, output format) |
| [summarization_and_expansion.py](summarization_and_expansion.py) | Summarizing and expanding the same text in one prompt, with constrained length and a fixed output format |
| [text_analysis.py](text_analysis.py) | Review analysis returned as strict JSON (sentiment, confidence, topics, emotions), including a sarcastic review |
| [text_transformation.py](text_transformation.py) | Rewriting one message as formal, casual, JSON and tweet-length versions |

Shared helpers live in [helper/llm_helpers.py](helper/llm_helpers.py):

- `get_response(model, temperature, max_tokens, messages)` sends a full message list with explicit settings.
- `get_prompt_response(prompt)` sends a single user prompt to the model set in `AI_MODEL`, with `reasoning_effort="low"`.

## Hugging Face examples

The scripts in [hugging_face/](hugging_face/) run models locally with `transformers` pipelines. They don't use OpenRouter or the helper module, and the models download on first run.

| Script | Pipeline and model | What it demonstrates |
| --- | --- | --- |
| [sentiment_analysis.py](hugging_face/sentiment_analysis.py) | `text-classification`, `distilbert-base-uncased-finetuned-sst-2-english` | Sentiment on single and batched texts, including sarcasm the model tends to misread |
| [grammar_check.py](hugging_face/grammar_check.py) | `text-classification`, `abdulmatinomotoso/English_Grammar_Checker` | Labeling sentences as grammatically acceptable or not |
| [qnli.py](hugging_face/qnli.py) | `text-classification`, `cross-encoder/qnli-electra-base` | Scoring whether a sentence answers a question (question and text pairs) |
| [dynamic_category_assignment.py](hugging_face/dynamic_category_assignment.py) | `zero-shot-classification`, `facebook/bart-large-mnli` | Assigning categories chosen at run time, with no training |
| [extractive_summarization.py](hugging_face/extractive_summarization.py) | `text-generation`, `Qwen/Qwen2.5-1.5B-Instruct` | Summarizing a text by prompting a small chat model |
| [abstractive_summarization.py](hugging_face/abstractive_summarization.py) | `text-generation`, `Qwen/Qwen2.5-1.5B-Instruct` | Summarizing "in your own words" with the same model |
| [document_qa.py](hugging_face/document_qa.py) | `question-answering`, `distilbert-base-cased-distilled-squad` | Extractive question answering over a PDF ([employee_policy.pdf](employee_policy.pdf)): text is read with `pypdf`, and the model returns the span of the document that answers each question |

## Setup

Requires Python 3.9 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
pip install transformers torch   # only for the hugging_face scripts
pip install pypdf                # only for hugging_face/document_qa.py
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
python summarization_and_expansion.py
python text_analysis.py
python text_transformation.py
python virtual_paris_tourist_chatbot.py   # type "exit" to quit
python hugging_face/sentiment_analysis.py # any script in hugging_face/ runs the same way
```

The exception is `document_qa.py`: it opens the PDF at `../employee_policy.pdf`, so run it from inside `hugging_face/`:

```bash
cd hugging_face && python document_qa.py
```

## Notes

- Running the OpenRouter scripts makes real API calls and may incur costs. The `hugging_face` scripts run locally and are free, but the first run downloads each model.
- `virtual_paris_tourist_chatbot.py` reuses `get_response` from the helper module and calls the model set in `AI_MODEL`. Replies are capped at 150 tokens.
