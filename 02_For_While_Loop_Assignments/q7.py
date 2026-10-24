# Q7. Calculate factorial of a number using for loop.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"Factorial of {num} is {factorial}")
