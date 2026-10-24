# Q48. Check whether number is strong number.

num = int(input("Enter a number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i
    total = total + factorial
    temp = temp // 10

if total == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")
