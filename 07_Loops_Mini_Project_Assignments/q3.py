# Mini Project 3: ATM PIN Verification
# Problem Statement: Simulate ATM access with a limited number of PIN attempts.
# Rules: sample PIN 1234, max 3 attempts, Access Granted on correct, Card Temporarily Locked after 3 wrong, show attempts used.

correct_pin = 1234
max_attempts = 3
attempts = 0
granted = False

while attempts < max_attempts:
    pin = int(input("Enter your PIN: "))
    attempts = attempts + 1
    if pin == correct_pin:
        print("Access Granted")
        granted = True
        break
    else:
        print(f"Wrong PIN. Attempts left: {max_attempts - attempts}")

print("Attempts used:", attempts)
if not granted:
    print("Access status: Card Temporarily Locked")
else:
    print("Access status: Access Granted")
