# Q34. Check whether a string is palindrome.

text = input("Enter a string: ")
reverse = text[::-1]

if text == reverse:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
