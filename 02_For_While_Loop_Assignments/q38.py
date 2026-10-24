# Q38. Find smallest digit in a number.

num = int(input("Enter a number: "))
smallest = 9
temp = abs(num)

if temp == 0:
    smallest = 0

while temp > 0:
    digit = temp % 10
    if digit < smallest:
        smallest = digit
    temp = temp // 10

print("Smallest digit =", smallest)
