# Q12. Reverse a number using while loop.

num = int(input("Enter a number: "))
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reversed number =", reverse)
