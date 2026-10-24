# Mini Project 4: Student Scholarship Eligibility
# Basic conditions: percentage >= 75, family income <= Rs.4,00,000
# and attendance >= 75. Percentage >= 90 gives a Full Scholarship.

student_name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
annual_income = float(input("Enter annual family income: Rs. "))
attendance = float(input("Enter attendance percentage: "))

# Collect the reason when a basic condition fails
reason = ""
if percentage < 75:
    reason = reason + " Percentage below 75%."
if annual_income > 400000:
    reason = reason + " Family income above Rs.4,00,000."
if attendance < 75:
    reason = reason + " Attendance below 75%."

print("\n--- Scholarship Result ---")
print("Student Name      :", student_name)

if reason == "":
    print("Eligibility Status: Eligible")
    if percentage >= 90:
        print("Scholarship Category: Full Scholarship")
    else:
        print("Scholarship Category: Partial Scholarship")
else:
    print("Eligibility Status: Not Eligible")
    print("Scholarship Category: None")
    print("Reason            :", reason.strip())
