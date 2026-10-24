# Mini Project 6: Hotel Room Booking System
# Standard Rs.2,000/night, Deluxe Rs.3,500/night, Suite Rs.6,000/night.
# 10% discount on a stay of 5+ nights, 20% on a stay of 10+ nights.

guest_name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ").strip().title()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Error: Number of nights must be greater than 0.")
elif room_type != "Standard" and room_type != "Deluxe" and room_type != "Suite":
    print("Error: Invalid room type.")
else:
    # Price per night based on room type
    if room_type == "Standard":
        rate_per_night = 2000
    elif room_type == "Deluxe":
        rate_per_night = 3500
    else:
        rate_per_night = 6000

    room_charge = rate_per_night * nights

    # Discount based on length of stay
    if nights >= 10:
        discount_percent = 20
    elif nights >= 5:
        discount_percent = 10
    else:
        discount_percent = 0

    discount = room_charge * discount_percent / 100
    final_amount = room_charge - discount

    print("\n--- Hotel Booking Bill ---")
    print("Guest Name       :", guest_name)
    print("Room Type        :", room_type)
    print("Number of Nights :", nights)
    print("Room Charge      : Rs.", room_charge)
    print("Discount         : Rs.", discount)
    print("Final Booking Amount: Rs.", final_amount)
