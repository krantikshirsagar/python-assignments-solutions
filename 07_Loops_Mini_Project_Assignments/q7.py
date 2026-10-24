# Mini Project 7: Employee Payroll Summary
# Problem Statement: Calculate payroll details for several employees.
# Rules: overtime Rs.200/hour, gross = basic + overtime, deduct 10% if gross >= 50000 else 5%, total net payroll.

employees = int(input("Enter number of employees: "))
total_net = 0

for i in range(1, employees + 1):
    name = input(f"\nEnter name of employee {i}: ")
    basic = float(input(f"Enter basic salary of {name}: "))
    overtime_hours = float(input(f"Enter overtime hours of {name}: "))
    overtime_pay = overtime_hours * 200
    gross = basic + overtime_pay
    if gross >= 50000:
        deduction = gross * 0.10
    else:
        deduction = gross * 0.05
    net = gross - deduction
    total_net = total_net + net
    print(f"{name}: Gross salary = {gross}, Deduction = {round(deduction, 2)}, Net salary = {round(net, 2)}")

print("\n--- Payroll Summary ---")
print("Employee count:", employees)
print("Total net payroll:", round(total_net, 2))
