# Q34. Write a program to check whether a year is a leap year and century year.

year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print(year, "is a century year and a leap year")
    else:
        print(year, "is a century year but not a leap year")
else:
    print(year, "is not a century year")
