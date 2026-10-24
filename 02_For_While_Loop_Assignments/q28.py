# Q28. Check whether a number is Armstrong.

num = int(input("Enter a number: "))
temp = num
total = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
