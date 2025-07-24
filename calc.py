# This program acts as a basic calculator.
# It takes two numbers and an operation from the user,
# performs the calculation, and displays the result.

def calculate():
    """
    Prompts the user for two numbers and an operation,
    then performs the calculation and prints the result.
    Handles potential errors like invalid input or division by zero.
    """
    print("Welcome to the Basic Calculator!")
    print("Thanks to PLP for this!)

    # Step 1: Get the first number from the user,
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Step 2: Get the second number from the user
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Step 3: Get the mathematical operation from the user
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            break # Exit loop if operation is valid
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

    # Step 4: Perform the calculation based on the operation
    result = None # Initialize result to None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return # Exit the function if division by zero occurs
        else:
            result = num1 / num2

    # Step 5: Print the result in the specified format
    if result is not None: # Only print if a valid result was calculated
        print(f"{num1} {operation} {num2} = {result}")

# Call the function to start the calculator
calculate()
