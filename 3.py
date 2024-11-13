# Adding two numbers
def add(a, b):
    return a + b

# Subtracting two numbers
def subtract(a,b):
    return a - b

# Multiplying two numbers
def multiply(a,b):
    return a * b

# Dividing two numbers
def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error!."

# Calculator Function
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # User Input
    choice = input("Enter choice (1/2/3/4): ")

    # Validation of choice
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Wrong input! Please enter a valid operation.")

# Run the calculator
if __name__ == "__main__":
    calculator()

