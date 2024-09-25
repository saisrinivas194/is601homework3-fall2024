import pytest
from calculator.calculator import Calculator
from calculator.calculation import Calculation, Calculations

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)

def test_calculation_add():
    calc = Calculation(2, 3, 'add')
    assert calc.result == 5

def test_add_calculation_to_history():
    Calculations.clear_history()
    calc = Calculation(2, 3, 'add')
    Calculations.add_calculation(calc)
    assert Calculations.get_last().result == 5

def test_clear_history():
    Calculations.clear_history()
    assert Calculations.get_last() is None

# Tests to ensure these branches are covered
def test_calculation_subtract():
    calc = Calculation(7, 3, 'subtract')
    assert calc.result == 4  # Check subtraction

def test_calculation_multiply():
    calc = Calculation(3, 4, 'multiply')
    assert calc.result == 12  # Check multiplication

def test_calculation_divide():
    calc = Calculation(8, 2, 'divide')
    assert calc.result == 4  # Check division

# Test to ensure ValueError is raised for unknown operation
def test_calculation_invalid_operation():
    with pytest.raises(ValueError):
        Calculation(5, 5, 'invalid_op')

def test_get_all_with_history():
    Calculations.clear_history()  # Start fresh
    calc1 = Calculation(1, 2, 'add')
    Calculations.add_calculation(calc1)  # Add a calculation
    assert Calculations.get_all() == [calc1]  # Check if get_all returns the correct history
