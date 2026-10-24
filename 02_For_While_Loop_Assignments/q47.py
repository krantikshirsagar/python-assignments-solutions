# Q47. Find product of digits of a number.

num = int(input("Enter a number: "))
product = 1
temp = abs(num)

if temp == 0:
    product = 0

while temp > 0:
    digit = temp % 10
    product = product * digit
    temp = temp // 10

print("Product of digits =", product)
