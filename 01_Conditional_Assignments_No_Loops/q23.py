# Q23. Write a program to calculate electricity bill based on units consumed.

# Assumed slab rates: first 100 units at Rs.5 per unit, next 100 at Rs.7, above 200 at Rs.10
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print("Electricity bill: Rs.", bill)
