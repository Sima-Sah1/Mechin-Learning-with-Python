# Ask the user for the number of Fibonacci terms
n = int(input("Enter the number of Fibonacci terms: "))

# Initialize the first two terms
a, b = 0, 1

# Print Fibonacci sequence
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
