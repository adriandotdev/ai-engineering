from transformers import pipeline

grammar_checker = pipeline(
    "text-classification",
    model="abdulmatinomotoso/English_Grammar_Checker"
)

print(grammar_checker("He eat pizza every day."))
print(grammar_checker("He eats pizza everyday."))