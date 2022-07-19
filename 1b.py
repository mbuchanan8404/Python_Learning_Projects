##############################
# Matthew Ryan Buchanan
# set 1.b
##############################


import math


# Add two numbers and print output
print( (50 + 50) + (100 - 10) )
# OR
num1 = 50 + 50
num2 = 100 - 10
total = num1 + num2
print(total)


# Test error output
# 30+*6,6^6,6**6,6+6+6+6+6+6


# Basic print test
print("Hello World\n")
print("Hello World : 10\n")


# Function to find necesarry monthly payment for a loan with principal p, interest rate r, and length to repayment in months l
# We'll give the user nice prompts for each input
p = float(input("Please input the amount of the loan:\n"))                        # Get the total principal from user
r = float(input("Please input the annual interest rate:\n")) / 100.0              # Get the annual interest rate as a whole number
l = int(input("Please input the total number of months to pay of the loan:\n"))   # Get the total number of months to pay off the loan

# Use the loan formula solved for monthly payment amount
monthly_payment = (p * (r / 12) * (1 + (r / 12)) ** l) / ((1 + r / 12) ** l - 1)

# Display required monthly payment rounded up to nearest dollar
print("The monthly payment you need to make is: $" + str(math.ceil(monthly_payment)))



