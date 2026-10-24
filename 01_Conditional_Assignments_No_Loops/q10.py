# Q10. Write a program to check whether a number is a single-digit number or not.

num = int(input("Enter a number: "))
if -9 <= num <= 9:
    print(num, "is a single-digit number")
else:
    print(num, "is not a single-digit number")
