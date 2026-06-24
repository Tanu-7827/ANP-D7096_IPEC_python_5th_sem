#Write a Python program to find how many slices remain after equal distribution. 
# Input the total number of pizza slices
total_slices = int(input("Enter the total number of slices: "))

# Input the number of people
people = int(input("Enter the number of people: "))

# Calculate the remaining slices
remaining_slices = total_slices % people

# Display the remaining slices
print("Remaining slices =", remaining_slices)