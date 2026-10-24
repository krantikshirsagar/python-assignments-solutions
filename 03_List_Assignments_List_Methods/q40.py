# Q40. Create a list and demonstrate all list methods.

numbers = [30, 10, 20]
print("Start:", numbers)

# append() - add at the end
numbers.append(40)
print("After append(40):", numbers)

# insert() - add at a specific index
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

# extend() - add elements of another list
numbers.extend([50, 60])
print("After extend([50, 60]):", numbers)

# remove() - remove a specific value
numbers.remove(15)
print("After remove(15):", numbers)

# pop() - remove and return an element (last by default)
removed = numbers.pop()
print("After pop():", numbers, "| Removed:", removed)

# count() - how many times a value appears
print("Count of 20:", numbers.count(20))

# index() - position of a value
print("Index of 20:", numbers.index(20))

# sort() - arrange in ascending order
numbers.sort()
print("After sort():", numbers)

# reverse() - reverse the order
numbers.reverse()
print("After reverse():", numbers)

# copy() - make a copy of the list
numbers_copy = numbers.copy()
print("Copy of the list:", numbers_copy)

# clear() - remove all elements (done on the copy, so the original stays)
numbers_copy.clear()
print("Copy after clear():", numbers_copy)
print("Original list (unchanged by clear on copy):", numbers)
