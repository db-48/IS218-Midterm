import pytest 
from calculator.calculations import Calculator
from calculator.plugins.commands import Command, Add_Command, Subtract_Command, Multiply_Command, Divide_Command

@pytest.fixture
def calculator():
    return Calculator()

def test_command_execute_not_implemented():
    command = Command()
    with pytest.raises(NotImplementedError):
        command.execute(1, 2)

def test_add_command(calculator):
    add_command = Add_Command()
    result = add_command.execute(3, 4)
    assert result == calculator.add(3, 4)

def test_subtract_command(calculator):
    subtract_command = Subtract_Command()
    result = subtract_command.execute(10, 4)
    assert result == calculator.subtract(10, 4)

def test_multiply_command(calculator):
    multiply_command = Multiply_Command()
    result = multiply_command.execute(3, 5)
    assert result == calculator.multiply(3, 5)

def test_divide_command(calculator):
    divide_command = Divide_Command()
    result = divide_command.execute(10, 2)
    assert result == calculator.divide(10, 2)

    with pytest.raises(ZeroDivisionError):
        divide_command.execute(10, 0)