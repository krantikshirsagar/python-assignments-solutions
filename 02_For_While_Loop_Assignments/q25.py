# Q25. Count consonants in a string.

text = input("Enter a string: ")
count = 0

for char in text.lower():
    if char.isalpha() and char not in "aeiou":
        count = count + 1

print("Number of consonants =", count)
