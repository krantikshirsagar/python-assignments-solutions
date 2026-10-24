# Mini Project 2: Online Shopping Checkout
# Discount slabs on purchase amount, extra 5% discount to Premium
# customers, free delivery when the payable amount is Rs.2,000 or more.

customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: Rs. "))
customer_type = input("Enter customer type (Regular/Premium): ").strip().title()

if purchase_amount < 0:
    print("Invalid purchase amount.")
else:
    # Discount based on purchase amount
    if purchase_amount >= 5000:
        discount_percent = 20
    elif purchase_amount >= 3000:
        discount_percent = 10
    elif purchase_amount >= 1000:
        discount_percent = 5
    else:
        discount_percent = 0

    # Additional discount to Premium customers
    if customer_type == "Premium":
        discount_percent = discount_percent + 5
    elif customer_type != "Regular":
        print("Note: Unknown customer type, treated as Regular.")

    discount_amount = purchase_amount * discount_percent / 100
    amount_after_discount = purchase_amount - discount_amount

    # Delivery charge based on the amount after discount
    if amount_after_discount >= 2000:
        delivery_charge = 0
    else:
        delivery_charge = 100

    final_amount = amount_after_discount + delivery_charge

    print("\n--- Shopping Checkout Bill ---")
    print("Customer Name      :", customer_name)
    print("Purchase Amount    : Rs.", purchase_amount)
    print("Discount Amount    : Rs.", discount_amount)
    print("Delivery Charge    : Rs.", delivery_charge)
    print("Final Payable Amount: Rs.", final_amount)
