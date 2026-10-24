# Q13. Join a list of words into a single string.

words_input = input("Enter words separated by comma: ")
words = [w.strip() for w in words_input.split(",")]
result = " ".join(words)
print("Joined string:", result)
