''' To calculate speed when distance and time are provided '''

# Input of distance from the user
distance = float(input("Enter the distance (in km): "))

# Validating the distance
if distance < 0:
    exit("Distance cannot be negative.")

# Input of time from the user
time = float(input("Enter the time (in hours): "))

# Validating the time
if time <= 0:
    exit("Time must be greater than zero.")

# -----------------------------------------------------

# Displaying data to the user
print("Distance:", distance, "km")
print("Time:", time, "hours")

# -----------------------------------------------------

# Displaying speed
print("Speed:", distance / time, "km/hr") 