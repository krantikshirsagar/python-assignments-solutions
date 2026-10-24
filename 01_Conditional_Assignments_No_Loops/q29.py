# Q29. Write a program to check blood donation eligibility based on age and weight.

# Assumed rules: age 18 to 65 and weight 50 kg or more
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
if 18 <= age <= 65 and weight >= 50:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")
