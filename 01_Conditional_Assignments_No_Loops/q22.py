# Q22. Write a program to check salary bonus based on years of service.

# Assumed bonus rules: more than 5 years = 10% of salary, 3-5 years = 5%, less than 3 years = no bonus
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.10
    print("Bonus: Rs.", bonus)
elif years >= 3:
    bonus = salary * 0.05
    print("Bonus: Rs.", bonus)
else:
    print("No bonus")
