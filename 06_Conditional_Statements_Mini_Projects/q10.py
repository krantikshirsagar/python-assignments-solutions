# Mini Project 10: Restaurant Bill and Service Charge
# Discount slabs on the food bill, extra 5% discount to members,
# then a 5% service charge on the amount after discount.

customer_name = input("Enter customer name: ")
food_bill = float(input("Enter food bill amount: Rs. "))
membership = input("Do you have a membership? (Yes/No): ").strip().title()

if food_bill < 0:
    print("Error: Food bill amount cannot be negative.")
else:
    # Discount based on bill amount
    if food_bill >= 5000:
        discount_percent = 15
    elif food_bill >= 3000:
        discount_percent = 10
    elif food_bill >= 1000:
        discount_percent = 5
    else:
        discount_percent = 0

    # Additional discount to members
    if membership == "Yes":
        discount_percent = discount_percent + 5

    discount = food_bill * discount_percent / 100
    amount_after_discount = food_bill - discount
    service_charge = amount_after_discount * 5 / 100
    final_amount = amount_after_discount + service_charge

    if final_amount >= 5000:
        message = "Thank you for being a valued customer"
    else:
        message = "Thank you for dining with us"

    print("\n--- Restaurant Bill ---")
    print("Customer Name    :", customer_name)
    print("Original Bill    : Rs.", food_bill)
    print("Discount         : Rs.", discount)
    print("Service Charge   : Rs.", service_charge)
    print("Final Payable Amount: Rs.", final_amount)
    print("Message          :", message)
