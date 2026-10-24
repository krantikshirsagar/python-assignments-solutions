# Q36. Remove duplicate characters from a string.

s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("Without duplicates:", result)
