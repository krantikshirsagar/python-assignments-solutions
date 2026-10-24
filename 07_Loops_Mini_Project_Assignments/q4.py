# Mini Project 4: Shopping Cart Total
# Problem Statement: Calculate a customer's shopping bill from multiple products.
# Rules: loop price*qty, subtotal, 10% discount if subtotal >= 3000, delivery Rs.100 if discounted amount < 1500 else free, reject negatives.

products = int(input("Enter number of products: "))
subtotal = 0

for i in range(1, products + 1):
    price = float(input(f"Enter price of product {i}: "))
    qty = int(input(f"Enter quantity of product {i}: "))
    if price < 0 or qty < 0:
        print("Invalid input! Price/quantity cannot be negative. Skipped.")
        continue
    item_total = price * qty
    print(f"Product {i} subtotal: {item_total}")
    subtotal = subtotal + item_total

if subtotal >= 3000:
    discount = subtotal * 0.10
else:
    discount = 0

after_discount = subtotal - discount
if after_discount < 1500:
    delivery = 100
else:
    delivery = 0

final = after_discount + delivery
print("\n--- Bill ---")
print("Subtotal:", subtotal)
print("Discount:", round(discount, 2))
print("Delivery charge:", delivery)
print("Final payable amount:", round(final, 2))
