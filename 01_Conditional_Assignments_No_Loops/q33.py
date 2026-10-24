# Q33. Write a program to check whether a person can apply for a loan.

# Assumed rules: age 21 to 60, monthly salary Rs.25000 or more, and no existing loan due noted simply by salary check
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
if 21 <= age <= 60 and salary >= 25000:
    print("You can apply and are eligible to get a loan")
else:
    print("You are not eligible to apply and get a loan")
