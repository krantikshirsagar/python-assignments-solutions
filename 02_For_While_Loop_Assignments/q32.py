# Q32. Calculate power of a number without using pow().

base = int(input("Enter base number: "))
power = int(input("Enter power: "))
result = 1

for i in range(power):
    result = result * base

print(f"{base} ^ {power} = {result}")
