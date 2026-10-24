# Q28. Write a program to calculate discounts based on total shopping amount.

# Assumed discount rules: 5000 and above = 20%, 2000 and above = 10%, 1000 and above = 5%, else no discount
amount = float(input("Enter total shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0
print("Discount: Rs.", discount)
print("Amount to pay: Rs.", amount - discount)
