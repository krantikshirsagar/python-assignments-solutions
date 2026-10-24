# Q23. Check whether a string is a palindrome.

s = input("Enter a string: ")
reversed_string = s[::-1]
if s == reversed_string:
    print("Palindrome: True")
else:
    print("Palindrome: False")
