import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    # Define operation mappings using Calculator methods
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        # Convert inputs to Decimal and handle invalid inputs
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)
        
        # Get the corresponding operation function, if exists
        operation_func = operation_mappings.get(operation_name)
        
        if operation_func:
            # Perform the operation and print the result
            result = operation_func(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            # Handle unknown operations
            print(f"Unknown operation: {operation_name}")
    
    # Handle cases where a or b cannot be converted to Decimal
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    
    # Handle division by zero specifically
    except ZeroDivisionError:
        print("Error: Division by zero.")
    
    # Catch-all for any other unexpected errors
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ensure correct usage and number of arguments
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    # Extract arguments and pass them to the function
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

# Run the main function only when this script is executed directly
if __name__ == '__main__':
    main()
