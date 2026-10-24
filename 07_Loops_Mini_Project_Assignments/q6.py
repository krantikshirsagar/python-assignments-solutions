# Mini Project 6: Electricity Usage Analyzer
# Problem Statement: Analyze daily electricity consumption over a selected period.
# Rules: loop daily usage, total/average, count days > 10 units, max usage, High Usage if total > 300.

days = int(input("Enter number of days: "))
total = 0
highest = 0
high_days = 0

for day in range(1, days + 1):
    units = float(input(f"Enter units consumed on day {day}: "))
    total = total + units
    if units > highest:
        highest = units
    if units > 10:
        high_days = high_days + 1

average = total / days if days > 0 else 0
print("\n--- Usage Summary ---")
print("Total units:", total)
print("Average usage:", round(average, 2))
print("High-usage day count (more than 10 units):", high_days)
print("Maximum daily usage:", highest)
if total > 300:
    print("Usage status: High Usage")
else:
    print("Usage status: Normal Usage")
