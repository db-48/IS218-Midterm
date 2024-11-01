import sys
import logging
import logging.config
from calculator.commands import Add_Command, Subtract_Command, Multiply_Command, Divide_Command
from calculator.plugins.remainder_command import Remainder_Command 
from calculator.plugins.history_management import show_history, clear_history
import os
from dotenv import load_dotenv

load_dotenv()

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():
    """Main REPL loop for calculator."""
    commands = {
        "add": Add_Command(),
        "subtract": Subtract_Command(),
        "multiply": Multiply_Command(),
        "divide": Divide_Command(),
        "remainder": Remainder_Command(),
    }
    logger.info("Calculator started.")

    while True:
        try:
            print("*\nHello! You've opened the Calculator!")
            print("\nAvailable Operations:")
            operations = ["add", "subtract", "multiply", "divide", "remainder"]

            for operation in operations:
                print(f" - {operation}")
        
            user_input = input("\nType a command (or 'exit' to close the program!): ")

            if user_input.lower() == "exit":
                print("\nYou've closed the calculator. Goodbye!")
                print("*\n")
                logger.info("Calculator exited.")
                break

            parts = user_input.split()
            command_name = parts[0]
            args = list(map(float, parts[1:]))
            
            if command_name in commands:
                result = commands[command_name].execute(*args)
                print(f"Result: {result}")
                logger.info(f"Executed command: {command_name} with args: {args}, result: {result}")
            else:
                print("Error: Unknown command.")
                logger.warning(f"Unknown command: {command_name}")
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
            logger.error("ValueError: Invalid input provided by the user.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            logger.error("ZeroDivisionError: Division by zero attempted.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logger.error(f"Unexpected error: {e}")
        
        print()

if __name__ == "__main__":
    main()