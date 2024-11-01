from calculator.calculations import Calculator

calculator = Calculator()

class Command:
    def execute(self, *args):
        raise NotImplementedError

class Add_Command(Command):
    def execute(self, a, b):
        return calculator.add(a, b)

class Subtract_Command(Command):
    def execute(self, a, b):
        return calculator.subtract(a, b)

class Multiply_Command(Command):
    def execute(self, a, b):
        return calculator.multiply(a, b)

class Divide_Command(Command):
    def execute(self, a, b):
        return calculator.divide(a, b)