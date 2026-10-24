"""
Mini Project 2: Password Strength Checker
Description: Evaluates a user-entered password and displays whether it
is Weak, Medium or Strong, based on its length and the presence of
uppercase letters, lowercase letters, digits and special characters.
"""

# Take password input from the user
password = input("Enter your password: ")

# --- Check all the conditions ---
has_length = len(password) >= 8
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_uppercase = True
    elif ch.islower():
        has_lowercase = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

# --- Give 1 point for every condition satisfied ---
score = 0
if has_length:
    score = score + 1
if has_uppercase:
    score = score + 1
if has_lowercase:
    score = score + 1
if has_digit:
    score = score + 1
if has_special:
    score = score + 1

# --- Decide the strength from the score ---
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

# --- Display the results ---
print("\n--- Password Strength Report ---")
print("Password Length          :", len(password))
print("Length at least 8 chars  :", has_length)
print("Has Uppercase Letters    :", has_uppercase)
print("Has Lowercase Letters    :", has_lowercase)
print("Has Digits               :", has_digit)
print("Has Special Characters   :", has_special)
print("Score (out of 5)         :", score)
print("Password Strength        :", strength)
