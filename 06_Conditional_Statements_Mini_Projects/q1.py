# Mini Project 1: Smart Electricity Bill Calculator
# Rates: first 100 units Rs.3/unit, next 100 units Rs.5/unit,
# above 200 units Rs.7/unit, plus a fixed service charge of Rs.150.

customer_name = input("Enter customer name: ")
units = int(input("Enter units consumed: "))

if units < 0:
    print("Customer Name    :", customer_name)
    print("Units Consumed   :", units)
    print("Transaction Status: Invalid - units cannot be negative")
else:
    # Calculate the energy charge slab-wise
    if units <= 100:
        energy_charge = units * 3
    elif units <= 200:
        energy_charge = (100 * 3) + ((units - 100) * 5)
    else:
        energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

    service_charge = 150
    final_bill = energy_charge + service_charge

    if final_bill > 5000:
        usage_message = "High Usage Bill"
    else:
        usage_message = "Normal Usage"

    print("\n--- Electricity Bill ---")
    print("Customer Name  :", customer_name)
    print("Units Consumed :", units)
    print("Energy Charge  : Rs.", energy_charge)
    print("Service Charge : Rs.", service_charge)
    print("Final Bill     : Rs.", final_bill)
    print("Usage Message  :", usage_message)
