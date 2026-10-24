# Q40. Print numbers which are perfect squares between 1 and 100.

for i in range(1, 101):
    root = int(i ** 0.5)
    if root * root == i:
        print(i)
