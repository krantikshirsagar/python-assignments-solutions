# Q50. Write a program to build a simple ATM menu using a match case.

# Assumed starting balance: Rs.10000
balance = 10000
print("ATM Menu: 1. Check Balance  2. Withdraw  3. Deposit  4. Exit")
choice = int(input("Enter your choice (1-4): "))
match choice:
    case 1:
        print("Your balance is: Rs.", balance)
    case 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful. New balance: Rs.", balance)
        else:
            print("Insufficient balance")
    case 3:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful. New balance: Rs.", balance)
    case 4:
        print("Thank you, visit again")
    case _:
        print("Invalid choice")
