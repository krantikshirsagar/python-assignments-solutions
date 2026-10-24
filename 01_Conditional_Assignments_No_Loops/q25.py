# Q25. Write a program to check whether a triangle is equilateral, isosceles, or scalene.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a == b == c:
    print("Triangle is equilateral")
elif a == b or b == c or a == c:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")
