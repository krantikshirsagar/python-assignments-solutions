# Q36. Create a list and remove all odd numbers.

numbers = [10, 15, 20, 25, 30, 35, 40]
print("Before:", numbers)
numbers = [num for num in numbers if num % 2 == 0]
print("After removing odd numbers:", numbers)
