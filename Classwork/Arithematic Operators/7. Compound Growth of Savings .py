'''Write a Python program to calculate the value of money after a certain number of years assuming it 
doubles every year.'''

# Input the initial amount of money
amount = float(input("Enter the initial amount: "))

# Input the number of years
years = int(input("Enter the number of years: "))

# Calculate the final amount
final_amount = amount * (2 ** years)

# Display the result
print("Value of money after", years, "years =", final_amount)