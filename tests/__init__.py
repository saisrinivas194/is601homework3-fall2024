import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data for various calculator operations.

    Yields tuples of (a, b, operation_name, operation_func, expected_result).
    """
    # Define operation mappings
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        # Generate b such that it may be zero in some cases for testing division by zero
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure b is not zero for division to prevent division by zero
        if operation_func == divide and b == Decimal('0'):
            b = Decimal('1')  # Change b to 1 to avoid division by zero

        try:
            expected = operation_func(a, b) if not (operation_func == divide and b == Decimal('0')) else "ZeroDivisionError"
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Add a command-line option to specify the number of test records to generate."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate dynamic tests with test data from Faker."""
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
                               for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
