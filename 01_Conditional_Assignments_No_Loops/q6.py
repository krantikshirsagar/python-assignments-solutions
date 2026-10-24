# Q6. Write a program to compare two numbers and print the greater one.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("Greater number is:", a)
elif b > a:
    print("Greater number is:", b)
else:
    print("Both numbers are equal")
