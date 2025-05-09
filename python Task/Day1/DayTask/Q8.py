import math

# Define the function
def calculate_area(radius):
    return math.pi * radius ** 2

# Ask the user for the radius
r = float(input("Enter the radius of the circle: "))

# Call the function and print the result
area = calculate_area(r)
print(f"The area of the circle is: {area:.2f}")
