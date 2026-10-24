# Q22. Find sum of even digits in a number.

num = int(input("Enter a number: "))
total = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        total = total + digit
    temp = temp // 10

print("Sum of even digits =", total)
