'''Write a Python program to determine how many complete rows can be formed.'''
# Input the total number of students/items
total = int(input("Enter the total number of students/items: "))

# Input the number of students/items in each row
per_row = int(input("Enter the number in each row: "))

# Calculate complete rows
complete_rows = total // per_row

# Display the result
print("Number of complete rows =", complete_rows)