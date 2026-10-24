# Q17. Create a list of mixed data types and display them.

mixed = [10, "python", 3.14, True, "hello"]
print("Mixed list:", mixed)
for item in mixed:
    print(item, "-", type(item).__name__)
