# Mini Project 1: Daily Expense Tracker
# Problem Statement: Record expenses for a chosen number of days and summarize spending.
# Rules: loop for each day, total/average, highest expense, Budget Alert if total > 5000.

days = int(input("Enter number of days: "))
total = 0
highest = 0

for day in range(1, days + 1):
    expense = float(input(f"Enter expense for day {day}: "))
    total = total + expense
    if expense > highest:
        highest = expense

average = total / days if days > 0 else 0

print("\n--- Expense Summary ---")
print("Total expense:", total)
print("Average daily expense:", round(average, 2))
print("Highest daily expense:", highest)
if total > 5000:
    print("Budget status: Budget Alert - total exceeds Rs.5000")
else:
    print("Budget status: Within budget")
