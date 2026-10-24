# Q49. Display menu-driven program using while loop.

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Square a number")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello!")
    elif choice == 2:
        num = int(input("Enter a number: "))
        print("Square =", num * num)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again")
