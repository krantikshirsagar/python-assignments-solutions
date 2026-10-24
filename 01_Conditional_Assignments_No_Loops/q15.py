# Q15. Write a program to check whether a number is divisible by both 3 and 7 or not.

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(num, "is divisible by both 3 and 7")
else:
    print(num, "is not divisible by both 3 and 7")
