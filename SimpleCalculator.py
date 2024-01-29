class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

# Example usage:
if __name__ == "__main__":
    calculator = SimpleCalculator()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        if choice == '1':
            result = calculator.add(num1, num2)
            operation = "addition"
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            operation = "subtraction"
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            operation = "multiplication"
        elif choice == '4':
            result = calculator.divide(num1, num2)
            operation = "division"

        print(f"The result of {operation} is: {result}")
    else:
        print("Invalid input. Please choose a valid operation (1/2/3/4).")
