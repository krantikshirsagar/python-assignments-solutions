# Q26. Print ASCII values of characters in a string.

text = input("Enter a string: ")

for char in text:
    print(char, "=", ord(char))
