# Q14. Write a program to check whether a given character is uppercase or lowercase.

ch = input("Enter a single character: ")
if ch.isupper():
    print(ch, "is uppercase")
elif ch.islower():
    print(ch, "is lowercase")
else:
    print("Please enter a letter")
