# Q33. Print reverse of a string.

text = input("Enter a string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reverse of string =", reverse)
