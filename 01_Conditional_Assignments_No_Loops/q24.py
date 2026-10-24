# Q24. Write a program to check exam results (Distinction, First Class, Pass, Fail).

# Assumed rules: 75 and above = Distinction, 60-74 = First Class, 40-59 = Pass, below 40 = Fail
marks = float(input("Enter marks: "))
if marks >= 75:
    print("Result: Distinction")
elif marks >= 60:
    print("Result: First Class")
elif marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
