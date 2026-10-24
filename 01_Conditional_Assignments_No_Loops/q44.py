# Q44. Write a program to check traffic signal actions using match case.

signal = input("Enter signal colour (red, yellow, green): ").lower()
match signal:
    case "red":
        print("Action: Stop")
    case "yellow":
        print("Action: Wait / Get ready")
    case "green":
        print("Action: Go")
    case _:
        print("Invalid signal colour")
