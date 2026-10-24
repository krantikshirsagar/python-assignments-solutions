# Q39. Write a program to check whether a number is greater than 0 and less than 100.

num = float(input("Enter a number: "))
if num > 0 and num < 100:
    print(num, "is greater than 0 and less than 100")
else:
    print(num, "is not in the range 1 to 99")
