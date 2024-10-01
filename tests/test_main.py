import pytest
from main import calculate_and_print  # Ensure the import path matches your project structure

# Parameterize the test function to test different scenarios, including successful operations and error cases
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_output", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Division by zero error case
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Unknown operation case
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Invalid input case with non-numeric string
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Another invalid input case
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_output, capsys):
    # Call the function with the given inputs
    calculate_and_print(a_string, b_string, operation_string)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Strip whitespace and compare the result to the expected output
    assert captured.out.strip() == expected_output
