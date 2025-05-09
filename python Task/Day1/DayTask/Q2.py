# Ask the user for their height in cm
height_cm = float(input("Enter your height in centimeters: "))

# Ask the user for their weight in kg
weight_kg = float(input("Enter your weight in kilograms: "))

# Convert height to meters and calculate BMI
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

# Print BMI rounded to 2 decimal places
print(f"Your BMI is: {bmi:.2f}")