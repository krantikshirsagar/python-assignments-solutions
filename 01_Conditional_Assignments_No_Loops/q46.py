# Q46. Write a program to print grade description using match case.

grade = input("Enter grade (A, B, C, F): ").upper()
match grade:
    case "A":
        print("Description: Excellent")
    case "B":
        print("Description: Good")
    case "C":
        print("Description: Average")
    case "F":
        print("Description: Fail")
    case _:
        print("Invalid grade")
