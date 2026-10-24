# Q25. Extract only alphabets from a string.

s = input("Enter a string: ")
alphabets = ""
for ch in s:
    if ch.isalpha():
        alphabets += ch
print("Alphabets:", alphabets)
