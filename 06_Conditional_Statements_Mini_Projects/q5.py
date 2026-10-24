# Mini Project 5: Employee Performance Bonus
# Bonus depends on experience and a performance rating of 1 to 5.

employee_name = input("Enter employee name: ")
monthly_salary = float(input("Enter monthly salary: Rs. "))
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1 to 5): "))

print("\n--- Employee Bonus Details ---")
print("Employee Name    :", employee_name)

if rating < 1 or rating > 5:
    print("Performance Message: Invalid rating. Rating must be between 1 and 5.")
else:
    # Decide the bonus percentage
    if rating < 3:
        bonus_percent = 0
    elif experience >= 10 and rating >= 4:
        bonus_percent = 20
    elif experience >= 5 and rating >= 4:
        bonus_percent = 15
    elif experience >= 2 and rating >= 3:
        bonus_percent = 10
    else:
        bonus_percent = 0

    bonus_amount = monthly_salary * bonus_percent / 100
    final_salary = monthly_salary + bonus_amount

    if rating == 5:
        performance_message = "Excellent Performer"
    elif rating >= 3:
        performance_message = "Good Performer"
    else:
        performance_message = "Needs Improvement"

    print("Bonus Percentage :", bonus_percent, "%")
    print("Bonus Amount     : Rs.", bonus_amount)
    print("Final Salary     : Rs.", final_salary)
    print("Performance Message:", performance_message)
