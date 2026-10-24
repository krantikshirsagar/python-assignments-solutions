# Q10. Find the index of a given character in a string.

s = input("Enter a string: ")
ch = input("Enter a character to find: ")
index = s.find(ch)
if index == -1:
    print("Character not found")
else:
    print("Index of character:", index)
