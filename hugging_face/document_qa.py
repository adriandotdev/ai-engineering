# NOTE: This pipeline is an extractive one.
from transformers import pipeline
from pypdf import PdfReader

# See the PDF for its content
reader = PdfReader("../employee_policy.pdf")

document_text = ""

for page in reader.pages:
    document_text += page.extract_text()
    
# Uncomment this if you want to print the extracted document text
# print(document_text)

qa_pipeline = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad"
)

questions = [
    "How many days of annual leave do employees get?", 
    "What is the daily meal allowance during travel?",
    "How long is the probation period?",
    "What's the limit for gifts from vendors?",
    "If I am in probation period, do I have annual leave?"
]

result = qa_pipeline(question=questions, context=document_text, handle_impossible_answer=True)

for i in range(len(questions)):
    print(f"\n{questions[i]}: Answer: {result[i]['answer']}")
