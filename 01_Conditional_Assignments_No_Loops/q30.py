# Q30. Write a program to check the type of number (single, double, or three digit).

num = int(input("Enter a number: "))
num = abs(num)
if num < 10:
    print("It is a single-digit number")
elif num < 100:
    print("It is a double-digit number")
elif num < 1000:
    print("It is a three-digit number")
else:
    print("It has more than three digits")
