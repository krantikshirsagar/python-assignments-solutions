# Q34. Find the ASCII value of each character in a string.

s = input("Enter a string: ")
for ch in s:
    print(ch, ":", ord(ch))
