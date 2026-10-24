# Mini Project 10: Multiplication Table and Number Analyzer
# Problem Statement: Print a multiplication table and analyze a range of integers.
# Rules: table 1 to 10, loop range, count even/odd, sum of range, validate start <= end.

num = int(input("Enter a positive integer for the table: "))
print(f"\nMultiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

start = int(input("\nEnter start of range: "))
end = int(input("Enter end of range: "))

if start > end:
    print("Invalid range! Start should not be greater than end.")
else:
    even_count = 0
    odd_count = 0
    total = 0
    for n in range(start, end + 1):
        total = total + n
        if n % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    print("\n--- Range Analysis ---")
    print("Even count:", even_count)
    print("Odd count:", odd_count)
    print("Sum of range:", total)
