#Write a Python program to calculate the final payable amount after applying the discount.

# Input the original price
price = float(input("Enter the original price: "))

# Input the discount percentage
discount = float(input("Enter the discount percentage: "))

# Calculate the discount amount
discount_amount = (price * discount) / 100

# Calculate the final payable amount
final_amount = price - discount_amount

# Display the final payable amount
print("Final Payable Amount =", final_amount)