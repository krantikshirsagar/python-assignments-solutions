# Q40. Count uppercase and lowercase letters separately.

s = input("Enter a string: ")
upper_count = 0
lower_count = 0
for ch in s:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
