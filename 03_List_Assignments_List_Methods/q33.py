# Q33. Create a list and find the second largest number.

numbers = [10, 40, 20, 50, 30]
print("List:", numbers)
largest = max(numbers)
second_largest = max(num for num in numbers if num != largest)
print("Second largest number:", second_largest)
