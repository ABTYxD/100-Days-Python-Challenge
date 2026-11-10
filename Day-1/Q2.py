# Question 2 — Simple calculator

# Create two variables:
# a = 45
# b = 15

# Print their:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Remainder

# Expected output:
# Addition: 60
# Subtraction: 30
# Multiplication: 675
# Division: 3.0
# Remainder: 0

a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))

print("\n")

print(f"Addition: {a+b}")
print(f"Substraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Remainder: {a%b}")