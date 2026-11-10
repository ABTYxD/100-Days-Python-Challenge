# Question 3 — Age calculator

# Write a program that:
# 1. Asks the user for their name.
# 2. Asks the user for their current age.
# 3. Calculates their age after 5 years.
# 4. Displays a personalised message.

# Example:
# Enter your name: Abhishek
# Enter your age: 19

# Hello Abhishek!
# Your age after 5 years will be 24.

name = input("Your name: ")
age = int(input("Please enter your age: "))

print(f"Hello {name}!, your age after 5 years will be {age+5}")