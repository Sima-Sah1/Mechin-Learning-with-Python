# Q3: a Python program that takes the user's 
# exam score and prints their grade based on the specified conditions.

# Ask the user for their exam score
score = int(input("Enter your exam score: "))

# print the grade
if score >= 90:
    print("Your grade is: A")
elif score >= 80:
    print("Your grade is: B")
elif score >= 70:
    print("Your grade is: C")
elif score >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
