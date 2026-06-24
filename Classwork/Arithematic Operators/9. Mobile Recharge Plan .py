#Write a Python program to calculate the total recharge amount based on the data pack selected. 

# Input the price of one data pack
pack_price = float(input("Enter the price of the data pack: "))

# Input the number of data packs selected
quantity = int(input("Enter the number of data packs selected: "))

# Calculate the total recharge amount
total_amount = pack_price * quantity

# Display the total recharge amount
print("Total Recharge Amount =", total_amount)