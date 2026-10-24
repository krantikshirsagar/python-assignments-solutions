# Mini Project 2: Student Marks and Grade Report
# Problem Statement: Process marks for multiple students and generate a class performance summary.
# Rules: grades 75+ A, 60-74 B, 50-59 C, 40-49 D, below 40 Fail; pass/fail count; class average; reject 0-100 outside.

students = int(input("Enter number of students: "))
total_marks = 0
pass_count = 0
fail_count = 0
valid = 0

for i in range(1, students + 1):
    name = input(f"\nEnter name of student {i}: ")
    marks = float(input(f"Enter marks of {name} (out of 100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks! Marks must be between 0 and 100. Skipped.")
        continue
    valid = valid + 1
    total_marks = total_marks + marks
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"
    if grade == "Fail":
        fail_count = fail_count + 1
    else:
        pass_count = pass_count + 1
    print(f"{name}: Marks = {marks}, Grade = {grade}")

average = total_marks / valid if valid > 0 else 0
print("\n--- Class Summary ---")
print("Class average:", round(average, 2))
print("Pass count:", pass_count)
print("Fail count:", fail_count)
