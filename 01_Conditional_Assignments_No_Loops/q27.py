# Q27. Write a program to check login status based on username and password.

# Assumed correct login: username = admin, password = admin123
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid username or password")
