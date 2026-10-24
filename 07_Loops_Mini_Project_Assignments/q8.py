# Mini Project 8: Quiz Application
# Problem Statement: Create a command-line quiz using a fixed set of questions.
# Rules: at least 5 questions, 1 point per correct answer, percentage, Excellent 80%+, Good 60-79%, Keep Practicing below 60%.

questions = [
    ("What is the capital of India?", "delhi"),
    ("What is 5 + 7?", "12"),
    ("Which language is this quiz written in?", "python"),
    ("What is the colour of the sky on a clear day?", "blue"),
    ("How many days are there in a week?", "7"),
    ("What is 10 * 3?", "30"),
]

score = 0
for i, (question, correct) in enumerate(questions, start=1):
    print(f"\nQ{i}. {question}")
    answer = input("Your answer: ").strip().lower()
    if answer == correct.lower():
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong! Correct answer is: {correct}")

percentage = (score / len(questions)) * 100 if questions else 0
print("\n--- Result ---")
print(f"Score: {score} / {len(questions)}")
print(f"Percentage: {round(percentage, 2)}%")
if percentage >= 80:
    print("Performance: Excellent")
elif percentage >= 60:
    print("Performance: Good")
else:
    print("Performance: Keep Practicing")
