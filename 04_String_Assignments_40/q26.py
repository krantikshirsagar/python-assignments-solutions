# Q26. Find the first and last occurrence of a character.

s = input("Enter a string: ")
ch = input("Enter a character: ")
first = s.find(ch)
last = s.rfind(ch)
if first == -1:
    print("Character not found")
else:
    print("First occurrence:", first)
    print("Last occurrence:", last)
