#Write a Python program to calculate how much each participant should pay. 

# Input the total expense amount
total_expense = float(input("Enter the total expense amount: "))

# Input the number of participants
participants = int(input("Enter the number of participants: "))

# Calculate the share of each participant
share = total_expense / participants

# Display the amount each participant should pay
print("Each participant should pay =", share)