# Q45. Write a program to print menu-based food selection using match case.

print("Menu: 1. Pizza  2. Burger  3. Pasta  4. Sandwich")
choice = int(input("Enter your choice (1-4): "))
match choice:
    case 1:
        print("You selected: Pizza - Rs.199")
    case 2:
        print("You selected: Burger - Rs.99")
    case 3:
        print("You selected: Pasta - Rs.149")
    case 4:
        print("You selected: Sandwich - Rs.79")
    case _:
        print("Invalid choice")
