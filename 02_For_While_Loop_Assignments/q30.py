# Q30. Generate first n even numbers.

n = int(input("Enter n: "))
count = 0
num = 2

while count < n:
    print(num)
    num = num + 2
    count = count + 1
