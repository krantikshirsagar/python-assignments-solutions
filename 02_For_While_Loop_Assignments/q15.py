# Q15. Find sum of digits of a number.

num = int(input("Enter a number: "))
total = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

print("Sum of digits =", total)
