# Q14. Print Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
