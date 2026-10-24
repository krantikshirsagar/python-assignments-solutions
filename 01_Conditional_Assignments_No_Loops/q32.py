# Q32. Write a program to check whether a student is eligible for an exam (attendance + marks).

# Assumed rules: attendance 75% or more and marks 40 or more
attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))
if attendance >= 75 and marks >= 40:
    print("Student is eligible to appear in the exam")
else:
    print("Student is not eligible to appear in the exam")
