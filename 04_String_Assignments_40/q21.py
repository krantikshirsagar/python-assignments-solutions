# Q21. Find the length of a string without using len().

s = input("Enter a string: ")
count = 0
for ch in s:
    count += 1
print("Length of string:", count)
