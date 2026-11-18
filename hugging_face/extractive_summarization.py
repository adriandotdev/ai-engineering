from transformers import pipeline

# DEPRECATED
# summarizer = pipeline("summarization", model="nyamuda/extractive-summarization")

# Use the text generation with chat model
summarizer = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")

text = """
The James Webb Space Telescope, launched in December 2021, is the largest and
most powerful space telescope ever built. It observes the universe in infrared
light, which lets it see through dust clouds and detect the faint glow of the
earliest galaxies. Since beginning science operations in 2022, it has captured
detailed images of distant galaxies, studied the atmospheres of exoplanets, and
revealed new details about star formation. Scientists say its data is already
reshaping theories about how quickly galaxies formed after the Big Bang.
"""

message_history = [
    {
        "role": "user",
        "content": f"Summarize the following text:\n\n[{text}]"
    }
]
print(summarizer(message_history)[0])

# result = summarizer(text)

# print(result[0]["summary_text"])

