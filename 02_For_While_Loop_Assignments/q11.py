# Q11. Count number of digits in a number.

num = int(input("Enter a number: "))
count = 0
temp = abs(num)

if temp == 0:
    count = 1

while temp > 0:
    count = count + 1
    temp = temp // 10

print("Number of digits =", count)
