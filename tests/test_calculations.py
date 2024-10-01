'''My Calculator Test'''

# Correct import order according to PEP 8
from decimal import Decimal
import pytest

# Import necessary classes and functions from the calculator package
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """Setup for calculation tests: clear history and add sample calculations."""
    # Clear any existing history for a clean test environment
    Calculations.clear_history()
    # Add sample calculations to the history for testing purposes
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a new calculation to the history."""
    # Create a new calculation
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    # Add the calculation to the history
    Calculations.add_calculation(calc)
    # Verify the latest calculation in history matches the one just added
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history."

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    # Retrieve the calculation history
    history = Calculations.get_history()
    # Ensure history contains 2 calculations as set up by the fixture
    assert len(history) == 2, "History does not contain the expected number of calculations."

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    # Clear the history
    Calculations.clear_history()
    # Ensure the history is now empty
    assert len(Calculations.get_history()) == 0, "History was not cleared."

def test_get_latest(setup_calculations):
    """Test retrieving the latest calculation from the history."""
    # Retrieve the latest calculation
    latest = Calculations.get_latest()
    # Ensure the latest calculation matches the last one added in the fixture
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not retrieve the correct latest calculation."

def test_find_by_operation(setup_calculations):
    """Test finding calculations by operation type."""
    # Find all calculations with the 'add' operation
    add_operations = Calculations.find_by_operation("add")
    # Verify that one calculation with 'add' operation exists
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation."
    
    # Find all calculations with the 'subtract' operation
    subtract_operations = Calculations.find_by_operation("subtract")
    # Verify that one calculation with 'subtract' operation exists
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation."

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when history is empty."""
    # Clear the history to ensure it's empty
    Calculations.clear_history()
    # Verify that the latest calculation is None in an empty history
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history."
