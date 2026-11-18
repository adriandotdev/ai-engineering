from transformers import pipeline

classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)

text1 = "Hey, DataCamp; we would like to feature your courses in our newsletter!"
categories1 = ["marketing", "sales", "support"]
output1 = classifier(text1, categories1)

# Support Ticket Routing
text2 = "I was charged twice this month"
categories2 = ["billing", "technical issue", "account access"]
output2 = classifier(text2, categories2)

# Sentiment
text3 = "I love this product, works great!"
categories3 = ["positive", "negative", "neutral"]
output3 = classifier(text3, categories3)

print(f"Output1 => Labels: {output1['labels']}, Score: {output1['scores']}")

print(f"\nOutput2 => Labels: {output2['labels']}, Score: {output2['scores']}")

print(f"\nOutput3 => Labels: {output3['labels']}, Score: {output3['scores']}")