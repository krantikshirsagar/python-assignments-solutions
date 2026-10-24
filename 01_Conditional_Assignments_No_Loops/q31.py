# Q31. Write a program to check whether a number is positive and even using nested if.

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print(num, "is positive and even")
    else:
        print(num, "is positive but not even")
else:
    print(num, "is not positive")
