# Question 1 — Personal information

# Create a Python program that:
# 1. Stores your name in a variable.
# 2. Stores your age in another variable.
# 3. Stores your college name.
# 4. Prints all three details in separate lines.

# Expected output:
# Name: Abhishek
# Age: 19
# College: UPES

print("-------- PERSONAL INFORMATION ---------")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
cname = input("Please enter name of your institution: ")

print(f"Name: {name}\nAge: {age}\nInstitution Name: {cname}")