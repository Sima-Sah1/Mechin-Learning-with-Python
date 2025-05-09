# Define the function
def is_palindrome(word):
    return word == word[::-1]

# Ask the user for a word
user_input = input("Enter a word: ")

# Check and print the result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
