from transformers import pipeline

analyze = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print(analyze("Wi-Fi is slower than a snail today"))
print(analyze("I love your character"))

samples = [
    "Oh great, another Monday meeting that could have been an email.",
    "Wow, I just love waiting 45 minutes for a cold pizza.",
    "Fantastic, my laptop died right before the deadline.",
    "Thanks for the help, you made it so much worse.",
    "Wi-Fi is slower than a snail today!",
]

print(f"\n{analyze(samples)}")