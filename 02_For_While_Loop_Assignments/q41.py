# Q41. Print numbers which are perfect cubes between 1 and 100

for i in range(1, 101):
    root = round(i ** (1 / 3))
    if root * root * root == i:
        print(i)
