''' To calculate the value of money after a certain number of years
    assuming it doubles every year '''

# Input of initial amount from the user
amount = float(input("Enter the initial amount (in Rs): "))

# Validating the amount
if amount < 0:
    exit("Amount cannot be negative.")

# Input of number of years from the user
years = int(input("Enter the number of years: "))

# Validating the years
if years < 0:
    exit("Number of years cannot be negative.")

# -----------------------------------------------------

# Displaying data to the user
print("Initial Amount: Rs", amount)
print("Number of Years:", years)

# -----------------------------------------------------

# Calculating the final value of money
final_amount = amount * (2 ** years)

# Displaying the final amount
print("Value of Money after", years, "years: Rs", final_amount)
'''output:
'''