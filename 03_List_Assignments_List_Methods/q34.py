# Q34. Create a list and find common elements between two lists.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
print("List 1:", list1)
print("List 2:", list2)
common = [item for item in list1 if item in list2]
print("Common elements:", common)
