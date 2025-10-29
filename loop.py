# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Loop until user chooses to exit
while True:
    print("\nSimple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        print("Result:", add(num1, num2))
    elif operator == '-':
        print("Result:", subtract(num1, num2))
    elif operator == '*':
        print("Result:", multiply(num1, num2))
    elif operator == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operator")

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Goodbye!")
        break
