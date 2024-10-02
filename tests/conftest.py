import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for various calculator operations"""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Avoid division by zero for the divide operation
        if operation_func == divide and b == Decimal('0'):
            b = Decimal('1')

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Add a command-line option to specify the number of test records to generate"""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate dynamic tests with test data from Faker"""
    num_records = metafunc.config.getoption("num_records")

    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        parameters = list(generate_test_data(num_records))
        
        # Check for operation_name or operation and map correctly
        if 'operation_name' in metafunc.fixturenames:
            metafunc.parametrize("a, b, operation_name, expected", [(a, b, op_name, expected) for a, b, op_name, _, expected in parameters])
        else:
            metafunc.parametrize("a, b, operation, expected", [(a, b, op_func, expected) for a, b, _, op_func, expected in parameters])
