from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(a, b, operation, expected):
    """
    Test Calculation class with various arithmetic operations.

    Ensures that the Calculation class correctly performs the operation
    on two Decimal operands and returns the expected result.

    Parameters:
        a (Decimal): First operand.
        b (Decimal): Second operand.
        operation (function): Arithmetic operation (add, subtract, etc.).
        expected (Decimal): Expected result.
    """
    calc = Calculation(a, b, operation)
    result = calc.perform()
    assert result == expected, f"Failed {operation.__name__} with {a} and {b}. Expected: {expected}, got: {result}"

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.

    Verifies that the string representation of a Calculation instance
    accurately reflects the operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, f"Expected: {expected_repr}, got: {repr(calc)}"

def test_divide_by_zero():
    """
    Test division by zero raises ValueError.

    Ensures that dividing by zero in the Calculation class raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
