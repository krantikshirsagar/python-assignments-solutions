# Q40. Write a program to check whether a password is valid using nested if.

# Assumed valid password rule: at least 8 characters, and contains both letters and numbers
password = input("Enter a password: ")
if len(password) >= 8:
    if not password.isalpha() and not password.isdigit():
        print("Password is valid")
    else:
        print("Password is invalid: it must contain both letters and numbers")
else:
    print("Password is invalid: it must have at least 8 characters")
