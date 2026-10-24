# Q48. Write a program to print language choice using match case.

print("Language choices: 1. English  2. Hindi  3. Marathi")
choice = int(input("Enter your choice (1-3): "))
match choice:
    case 1:
        print("You selected: English")
    case 2:
        print("You selected: Hindi")
    case 3:
        print("You selected: Marathi")
    case _:
        print("Invalid choice")
