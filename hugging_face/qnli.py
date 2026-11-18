from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="cross-encoder/qnli-electra-base"
)

pairs = [
    {"text": "Where is Tokyo?", "text_pair": "Tokyo is located in Japan"},
    {"text": "Where is Tokyo?", "text_pair": "Tokyo is located in California"},
    {"text": "Where is Tokyo?", "text_pair": "Paris is known for its cuisine"},
    {"text": "Where is Tokyo?", "text_pair": "The city has a population of about 14 million"},
]
for p in pairs:
    print(p["text_pair"], classifier(p))