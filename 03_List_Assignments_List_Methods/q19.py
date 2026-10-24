# Q19. Create a list of 10 numbers and remove duplicates.

numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60, 40]
print("Before:", numbers)
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("After removing duplicates:", unique)
