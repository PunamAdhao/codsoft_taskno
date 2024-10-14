"""Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation choice
    operation = input("Enter your choice (1/2/3/4): ")

    # Validate operation choice
    if operation in ['1', '2', '3', '4']:
        try:
            # Get user input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            return

        # Perform calculation based on user choice
        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} = {result}")
    else:
        print("Invalid operation choice! Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    calculator()
