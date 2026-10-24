# Q37. Create a list and check palindrome list.

numbers = [10, 20, 30, 20, 10]
print("List:", numbers)
if numbers == numbers[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
