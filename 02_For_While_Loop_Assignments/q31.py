# Q31. Generate first n odd numbers.

n = int(input("Enter n: "))
count = 0
num = 1

while count < n:
    print(num)
    num = num + 2
    count = count + 1
