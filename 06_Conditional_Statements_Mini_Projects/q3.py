# Mini Project 3: ATM Withdrawal System
# Checks balance, a per-transaction limit of Rs.20,000, and warns
# when the remaining balance falls below Rs.1,000.

account_holder = input("Enter account holder name: ")
current_balance = float(input("Enter current balance: Rs. "))
withdrawal_amount = float(input("Enter withdrawal amount: Rs. "))

print("\n--- ATM Transaction ---")
print("Account Holder Name:", account_holder)

if withdrawal_amount <= 0:
    print("Transaction Status : Failed")
    print("Rejection Reason   : Withdrawal amount must be greater than Rs.0")
elif withdrawal_amount > 20000:
    print("Transaction Status : Failed")
    print("Rejection Reason   : Amount exceeds the per-transaction limit of Rs.20,000")
elif withdrawal_amount > current_balance:
    print("Transaction Status : Failed")
    print("Rejection Reason   : Insufficient balance")
else:
    remaining_balance = current_balance - withdrawal_amount
    print("Transaction Status : Successful")
    print("Withdrawn Amount   : Rs.", withdrawal_amount)
    print("Remaining Balance  : Rs.", remaining_balance)
    if remaining_balance < 1000:
        print("Message            : Low Balance Warning")
