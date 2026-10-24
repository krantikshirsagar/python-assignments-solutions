# Q36. Find sum of numbers entered by user until 0 is entered.

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total = total + num

print("Sum of numbers =", total)
