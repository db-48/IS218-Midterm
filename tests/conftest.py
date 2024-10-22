import pytest
from calculator.calculations import Calculator

@pytest.fixture
def calculator():
    return Calculator()
