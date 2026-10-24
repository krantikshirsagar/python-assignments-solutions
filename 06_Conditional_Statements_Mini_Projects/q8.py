# Mini Project 8: Movie Ticket Booking
# Base price Rs.200. Children below 12: 50% discount, senior citizens
# (60+): 30% discount, morning show: Rs.30 extra discount,
# weekend show: Rs.50 surcharge.

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ").strip().title()
day_type = input("Enter day type (Weekday/Weekend): ").strip().title()

if age < 0:
    print("Error: Age cannot be negative.")
else:
    base_price = 200

    # Age-based discount
    if age < 12:
        discount = base_price * 50 / 100
    elif age >= 60:
        discount = base_price * 30 / 100
    else:
        discount = 0

    # Morning show discount
    if show_type == "Morning":
        discount = discount + 30

    # Weekend surcharge
    if day_type == "Weekend":
        weekend_surcharge = 50
    else:
        weekend_surcharge = 0

    final_price = base_price - discount + weekend_surcharge
    if final_price < 0:
        final_price = 0

    print("\n--- Movie Ticket Bill ---")
    print("Customer Name      :", customer_name)
    print("Original Ticket Price: Rs.", base_price)
    print("Discount           : Rs.", discount)
    print("Weekend Surcharge  : Rs.", weekend_surcharge)
    print("Final Ticket Price : Rs.", final_price)
