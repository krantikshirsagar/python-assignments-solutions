# Q44. Print alternate characters of a string.

text = input("Enter a string: ")

print("Alternate characters:")
for i in range(0, len(text), 2):
    print(text[i])
