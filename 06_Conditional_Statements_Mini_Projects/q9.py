# Mini Project 9: Insurance Premium Calculator
# Base premium Rs.10,000. Age above 50: +Rs.5,000, high-risk job:
# +Rs.7,000, medium-risk job: +Rs.3,000, smoker: +Rs.5,000.
# Age below 18 is not eligible.

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
occupation_risk = input("Enter occupation risk (Low/Medium/High): ").strip().title()
smoker = input("Are you a smoker? (Yes/No): ").strip().title()

print("\n--- Insurance Premium Details ---")
print("Customer Name    :", customer_name)

if age < 18:
    print("Eligibility      : Not Eligible (age below 18)")
else:
    base_premium = 10000
    additional_charges = 0

    if age > 50:
        additional_charges = additional_charges + 5000

    if occupation_risk == "High":
        additional_charges = additional_charges + 7000
    elif occupation_risk == "Medium":
        additional_charges = additional_charges + 3000

    if smoker == "Yes":
        additional_charges = additional_charges + 5000

    final_premium = base_premium + additional_charges

    if additional_charges >= 10000:
        risk_message = "High Risk Policy"
    else:
        risk_message = "Normal Risk Policy"

    print("Eligibility      : Eligible")
    print("Base Premium     : Rs.", base_premium)
    print("Additional Charges: Rs.", additional_charges)
    print("Final Premium    : Rs.", final_premium)
    print("Risk Message     :", risk_message)
