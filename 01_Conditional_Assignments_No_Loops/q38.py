# Q38. Write a program to check whether a student passed all subjects.

# Assumed: marks in 3 subjects, pass mark in each subject is 40
s1 = float(input("Enter marks in subject 1: "))
s2 = float(input("Enter marks in subject 2: "))
s3 = float(input("Enter marks in subject 3: "))
if s1 >= 40 and s2 >= 40 and s3 >= 40:
    print("Student passed all subjects")
else:
    print("Student did not pass all subjects")
