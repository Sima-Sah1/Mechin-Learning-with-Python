# Define the function
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ask the user for input
number = int(input("Enter a positive integer: "))

# Call the function and print result
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a composite number.")
