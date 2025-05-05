while True:
    number = int(input("Enter a positive number (negative to stop): "))
    if number < 0:
        print("Negative number entered. Program stopped.")
        break
    else:
        print(f"You entered: {number}")
