# Q43. Write a program to print month days using match case.

# February is shown as 28 days (29 in a leap year)
month = int(input("Enter month number (1-12): "))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("This month has 31 days")
    case 4 | 6 | 9 | 11:
        print("This month has 30 days")
    case 2:
        print("This month has 28 days (29 in a leap year)")
    case _:
        print("Invalid month number")
