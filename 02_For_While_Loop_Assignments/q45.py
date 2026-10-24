# Q45. Print numbers skipping multiples of 3.

for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
