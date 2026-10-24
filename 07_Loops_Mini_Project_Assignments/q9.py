# Mini Project 9: Bank Transaction History
# Problem Statement: Process deposits and withdrawals and summarize a bank account's activity.
# Rules: deposits increase balance, withdrawals only if sufficient funds, count deposits/successful/rejected withdrawals, warn if final < 1000.

balance = float(input("Enter opening balance: "))
transactions = int(input("Enter number of transactions: "))
deposit_count = 0
withdraw_success = 0
withdraw_rejected = 0

for i in range(1, transactions + 1):
    print(f"\nTransaction {i}:")
    t_type = input("Enter type (deposit/withdraw): ").strip().lower()
    amount = float(input("Enter amount: "))
    if amount < 0:
        print("Invalid amount! Skipped.")
        continue
    if t_type == "deposit":
        balance = balance + amount
        deposit_count = deposit_count + 1
        print("Transaction status: Deposit successful")
    elif t_type == "withdraw":
        if amount <= balance:
            balance = balance - amount
            withdraw_success = withdraw_success + 1
            print("Transaction status: Withdrawal successful")
        else:
            withdraw_rejected = withdraw_rejected + 1
            print("Transaction status: Withdrawal rejected - insufficient funds")
    else:
        print("Transaction status: Invalid type. Use deposit or withdraw.")
    print("Current balance:", balance)

print("\n--- Account Summary ---")
print("Final balance:", balance)
print("Deposit count:", deposit_count)
print("Successful withdrawal count:", withdraw_success)
print("Rejected withdrawal count:", withdraw_rejected)
if balance < 1000:
    print("Warning: Balance is below Rs.1000")
