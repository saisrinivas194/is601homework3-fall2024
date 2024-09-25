from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_perform_addition():
    """Test the perform method for addition."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Addition perform failed"

def test_calculation_perform_subtraction():
    """Test the perform method for subtraction."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtraction perform failed"

def test_calculation_perform_multiplication():
    """Test the perform method for multiplication."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiplication perform failed"

def test_calculation_perform_division():
    """Test the perform method for division."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Division perform failed"

def test_calculation_repr_addition():
    """Test the __repr__ method of Calculation for addition."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), add)
    assert repr(calculation) == "Calculation(10, 5, add)", "Representation failed"

def test_calculation_repr_subtraction():
    """Test the __repr__ method of Calculation for subtraction."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), subtract)
    assert repr(calculation) == "Calculation(10, 5, subtract)", "Representation failed"

def test_calculation_repr_multiplication():
    """Test the __repr__ method of Calculation for multiplication."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), multiply)
    assert repr(calculation) == "Calculation(10, 5, multiply)", "Representation failed"

def test_calculation_repr_division():
    """Test the __repr__ method of Calculation for division."""
    calculation = Calculation.create(Decimal('10'), Decimal('5'), divide)
    assert repr(calculation) == "Calculation(10, 5, divide)", "Representation failed"
