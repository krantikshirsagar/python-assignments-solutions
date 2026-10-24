# Q47. Write a program to check user role (admin, user, guest) using match case.

role = input("Enter role (admin, user, guest): ").lower()
match role:
    case "admin":
        print("Welcome Admin - you have full access")
    case "user":
        print("Welcome User - you have limited access")
    case "guest":
        print("Welcome Guest - you have view-only access")
    case _:
        print("Unknown role")
