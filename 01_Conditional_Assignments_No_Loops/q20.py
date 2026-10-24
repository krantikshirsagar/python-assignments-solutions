# Q20. Write a program to check ticket price based on age.

# Assumed ticket prices: below 5 free, 5-12 Rs.100, 13-59 Rs.200, 60 and above Rs.150
age = int(input("Enter age: "))
if age < 5:
    print("Ticket price: Free")
elif age <= 12:
    print("Ticket price: Rs.100")
elif age < 60:
    print("Ticket price: Rs.200")
else:
    print("Ticket price: Rs.150")
