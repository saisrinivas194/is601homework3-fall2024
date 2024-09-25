from .calculator import Calculator

class Calculation:
    def __init__(self, operand1: float, operand2: float, operation: str):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
        self.result = self.perform_operation()

    def perform_operation(self) -> float:
        if self.operation == 'add':
            return Calculator.add(self.operand1, self.operand2)
        elif self.operation == 'subtract':
            return Calculator.subtract(self.operand1, self.operand2)
        elif self.operation == 'multiply':
            return Calculator.multiply(self.operand1, self.operand2)
        elif self.operation == 'divide':
            return Calculator.divide(self.operand1, self.operand2)
        else:
            raise ValueError("Unknown operation")


class Calculations:
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_last(cls) -> Calculation:
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @classmethod
    def get_all(cls) -> list:
        return cls.history