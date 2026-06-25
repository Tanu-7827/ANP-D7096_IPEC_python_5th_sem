''' To calculate area and perimeter of a rectangle '''

# Input of length from the user
length = float(input("Enter the length of the rectangle: "))

# Validating the length
if length < 0:
    exit("Length cannot be negative.")

# Input of breadth from the user
breadth = float(input("Enter the breadth of the rectangle: "))

# Validating the breadth
if breadth < 0:
    exit("Breadth cannot be negative.")

# -----------------------------------------------------

# Displaying data to the user
print("Length:", length)
print("Breadth:", breadth)

# -----------------------------------------------------

# Displaying area of the rectangle
print("Area of Rectangle:", length * breadth)

# Displaying perimeter of the rectangle
print("Perimeter of Rectangle:", 2 * (length + breadth))
