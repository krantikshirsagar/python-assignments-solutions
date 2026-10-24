# Q17. Find largest digit in a number.

num = int(input("Enter a number: "))
largest = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10

print("Largest digit =", largest)
