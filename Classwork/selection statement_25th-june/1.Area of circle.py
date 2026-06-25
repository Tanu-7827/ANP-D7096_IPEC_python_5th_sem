''' To calculate the area of a circle. '''
#input of radius.
radius = float(input("Enter the radius of the circle: "))
#validating the radius
if radius < 0:
    exit("Radius cannot be negative.")
#-----------------------------------------------------
#displaying data to the user
print("Radius of the circle: ", radius)
#-----------------------------------------------------
#displaying area of the circle
print("Area of the circle: ", 3.14 * radius * radius)  

'''output:
Radius of the circle:  5.0
Area of the circle:  78.5'''