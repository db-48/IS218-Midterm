from calculator.commands import Command

class Remainder_Command(Command):
    def execute(self, a: float, b: float) -> float:
        return a % b