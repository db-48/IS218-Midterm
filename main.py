import sys
from calculator.commands import Add_Command, Subtract_Command, Multiply_Command, Divide_Command

def main():
    """Main REPL loop for calculator."""
    commands = {
        "add command": Add_Command(),
        "subtract command": Subtract_Command(),
        "multiply command": Multiply_Command(),
        "divide command": Divide_Command(),
    }

    while True:
        try:
            print("*\nHello! You've opened the Calculator.")
            print("Avaliable Operations: add, subtract, multiply, divide")
            user_input = input("Type a command (or 'exit' to close the program! ): ")
            if user_input.lower() == "exit":
                break

            parts = user_input.split()
            command_name = parts[0]
            args = list(map(float, parts[1:]))
            
            if command_name in commands:
                result = commands[command_name].execute(*args)
                print(f"Result: {result}")
            else:
                print("Error: Unknown command.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print()

if __name__ == "__main__":
    main()