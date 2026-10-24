# Q17. Write a program to check grade based on marks (A, B, C, Fail).

# Assumed grade rules: 80 and above = A, 60-79 = B, 40-59 = C, below 40 = Fail
marks = float(input("Enter marks: "))
if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
