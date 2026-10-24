# Q35. Print multiplication tables from 1 to 5.

for num in range(1, 6):
    print(f"\nTable of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
