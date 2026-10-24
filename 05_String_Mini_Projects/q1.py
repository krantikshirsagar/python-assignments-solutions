"""
Mini Project 1: Text Analyzer System
Description: Takes a sentence or paragraph from the user and performs
multiple string-based analyses - counts, case conversion, word search,
word frequency and removing extra spaces.
"""

# Take input from the user
text = input("Enter a sentence or paragraph: ")
search_word = input("Enter a word to search in the text: ")

# --- Remove extra spaces ---
# split() breaks the text into words and join() joins them with one space
clean_text = " ".join(text.split())

# --- Basic counts ---
total_characters = len(text)
words = clean_text.split()
total_words = len(words)

# A sentence ends with '.', '!' or '?'
sentence_count = text.count(".") + text.count("!") + text.count("?")
if sentence_count == 0 and total_words > 0:
    sentence_count = 1

# --- Count vowels, consonants, digits and special characters ---
vowels = 0
consonants = 0
digits = 0
special_characters = 0

for ch in text:
    if ch.isdigit():
        digits = digits + 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    elif ch != " ":
        special_characters = special_characters + 1

# --- Case conversion ---
uppercase_text = text.upper()
lowercase_text = text.lower()

# --- Check whether a word exists ---
if search_word.lower() in clean_text.lower():
    word_found = "Yes, the word '" + search_word + "' is present in the text."
else:
    word_found = "No, the word '" + search_word + "' is not present in the text."

# --- Word frequency ---
word_frequency = {}
for word in words:
    clean_word = word.strip(".,!?;:").lower()
    if clean_word in word_frequency:
        word_frequency[clean_word] = word_frequency[clean_word] + 1
    else:
        word_frequency[clean_word] = 1

# --- Display the results ---
print("\n--- Text Analysis Report ---")
print("Original Text        :", text)
print("Text without extra spaces:", clean_text)
print("Total Characters     :", total_characters)
print("Total Words          :", total_words)
print("Total Sentences      :", sentence_count)
print("Vowels               :", vowels)
print("Consonants           :", consonants)
print("Digits               :", digits)
print("Special Characters   :", special_characters)
print("Uppercase Version    :", uppercase_text)
print("Lowercase Version    :", lowercase_text)
print("Word Search          :", word_found)
print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)
