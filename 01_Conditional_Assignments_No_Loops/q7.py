# Q7. Write a program to check whether a character is a vowel or consonant.

ch = input("Enter a single character: ").lower()
if ch in "aeiou":
    print(ch, "is a vowel")
elif ch.isalpha():
    print(ch, "is a consonant")
else:
    print("Please enter a letter")
