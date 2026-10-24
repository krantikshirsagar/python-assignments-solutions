# Mini Project 7: Mobile Data Plan Bill
# Basic Rs.299 (10 GB included), Standard Rs.499 (25 GB included),
# Premium Rs.799 (50 GB included). Extra data: Rs.20 per GB,
# plus a Rs.100 surcharge when extra data exceeds 10 GB.

customer_name = input("Enter customer name: ")
plan_type = input("Enter plan type (Basic/Standard/Premium): ").strip().title()
extra_data = float(input("Enter extra data used in GB: "))

if extra_data < 0:
    print("Error: Extra data usage cannot be negative.")
elif plan_type != "Basic" and plan_type != "Standard" and plan_type != "Premium":
    print("Error: Invalid plan type.")
else:
    # Base charge and included data based on plan type
    if plan_type == "Basic":
        base_charge = 299
        included_data = 10
    elif plan_type == "Standard":
        base_charge = 499
        included_data = 25
    else:
        base_charge = 799
        included_data = 50

    extra_data_charge = extra_data * 20

    if extra_data > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base_charge + extra_data_charge + surcharge

    print("\n--- Mobile Data Plan Bill ---")
    print("Customer Name    :", customer_name)
    print("Plan Type        :", plan_type)
    print("Included Data    :", included_data, "GB")
    print("Base Plan Charge : Rs.", base_charge)
    print("Extra Data Charge: Rs.", extra_data_charge)
    print("Surcharge        : Rs.", surcharge)
    print("Final Bill       : Rs.", final_bill)
