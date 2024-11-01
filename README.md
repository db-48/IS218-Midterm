## Project Overview
This is the calculator project assigned for the IS 218 Midterm. The calculator is able to: 1. perform arithmetic operations 2. Add, Subtract, Multiply, and Divide 3.Keep track of calculation history and Use extra features through plugins that can be loaded as needed

## Demonstration Video: - [here](https://youtu.be/hu9YFdeSkV8)

## Core Functionalities

### Command-Line Interface (REPL)
This program allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division; add: Returns the sum of two numbers, subtract: returns the difference of two numbers, multiply: returns the product of two numbers, divide: returns the quotient of two numbers.
These basic operations are found in [calculator/plugins/commands](https://github.com/db-48/IS218-Midterm/blob/main/calculator/plugins/commands.py) It also tracks calculation history by saving, showing and clearing history as per user input; show_history: Displays the calculation history, printing each command with its arguments and result, or notifies the user if no history is available, clear_history: Resets the calculation history by returning an empty DataFrame with predefined columns, save_entry: Saves a new entry to the calculation history, creating a DataFrame with the command name, arguments, and result, and combines it with the existing history if it’s not empty. These functions are found under [calculator/plugins/history_management](https://github.com/db-48/IS218-Midterm/blob/main/calculator/plugins/history_management.py) plugins/history_management. 

### Plugin System

Create a flexible plugin system to allow seamless integration of new commands or features. This system should:
- Dynamically load and integrate plugins without modifying the core application code.
- Include a REPL  "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

### Calculation History Management with Pandas

Utilize Pandas to manage a robust calculation history, enabling users to:
- Load, save, clear ~~and delete ,~~ history records through the REPL interface.


### Professional Logging Practices

Establish a comprehensive logging system to record:
- Detailed application operations, data manipulations, errors, and informational messages.
- Differentiate log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- Dynamic logging configuration through environment variables for levels and output destinations.

### Advanced Data Handling with Pandas

Employ Pandas for:
- Efficient data reading and writing to CSV files.
- Managing calculation history.

### Design Patterns for Scalable Architecture

Incorporate key design patterns to address software design challenges, including:
- **Facade Pattern:** Offer a simplified interface for complex Pandas data manipulations.
- **Command Pattern:** Structure commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns:** Further enhance the application's code structure, flexibility, and scalability.

## Development, Testing, and Documentation Requirements

### Testing and Code Quality

- Achieve a minimum of 90% test coverage with Pytest.
- ~~Ensure code quality and adherence to PEP 8 standards, verified by Pylint.~~

### Version Control Best Practices

- Utilize logical commits that clearly group feature development and corresponding tests, evidencing clear development progression.

### Comprehensive Documentation

- Compile detailed documentation in `README.md`, covering setup instructions, usage examples, and an in-depth analysis of architectural decisions, particularly emphasizing the implementation and impact of chosen design patterns and the logging strategy.


