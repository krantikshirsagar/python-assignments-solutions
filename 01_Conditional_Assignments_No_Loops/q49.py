# Q49. Write a program to print result status using match case.

status = input("Enter result status (pass, fail): ").lower()
match status:
    case "pass":
        print("Result: You have passed the exam")
    case "fail":
        print("Result: You have failed the exam")
    case _:
        print("Invalid result status")
