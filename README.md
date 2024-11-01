## Project Overview
This is the calculator project assigned for the IS 218 Midterm. The calculator is able to: 1. perform arithmetic operations 2. Add, Subtract, Multiply, and Divide 3.Keep track of calculation history and Use extra features through plugins that can be loaded as needed. The code passes pytest as well as pytest --cov. 

## Demonstration Video: [here](https://youtu.be/6gj2ftfOT-A)

## Core Functionalities

### Command-Line Interface (REPL)
This program allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division; add: Returns the sum of two numbers, subtract: returns the difference of two numbers, multiply: returns the product of two numbers, divide: returns the quotient of two numbers.
These basic operations are found in [calculator/plugins/commands](https://github.com/db-48/IS218-Midterm/blob/main/calculator/plugins/commands.py) It also tracks calculation history by saving, showing and clearing history as per user input; show_history: Displays the calculation history, printing each command with its arguments and result, or notifies the user if no history is available, clear_history: Resets the calculation history by returning an empty DataFrame with predefined columns, save_entry: Saves a new entry to the calculation history, creating a DataFrame with the command name, arguments, and result, and combines it with the existing history if it’s not empty. These functions are found under [calculator/plugins/history_management](https://github.com/db-48/IS218-Midterm/blob/main/calculator/plugins/history_management.py). 

### Plugin System
The function load_plugins: Loads command classes from the specified plugin module and adds them to the commands dictionary, logging successful loads or errors encountered during the process. This function is found in [calculator/plugins/plugin_loader](https://github.com/db-48/IS218-Midterm/blob/main/calculator/plugins/plugin_loader.py). The function attempts to import a module named `calculator.plugins.commands` using the `importlib` library. It then iterates through the module's attributes, looking for any callable classes that end with `_Command`, creates an instance of each class, and adds it to the `commands` dictionary with a lowercase version of the class name as the key. If the module cannot be found or any other error occurs during the loading process, the function displays an error message. There is also an addition feature new command which allows to the user to create an additional operation if need. This function is found in [main.py](https://github.com/db-48/IS218-Midterm/blob/main/main.py). 

### Calculation History Management with Pandas

Utilize Pandas to manage a robust calculation history, enabling users to:
- Load, save, clear ~~and delete ,~~ history records through the REPL interface.


### Professional Logging Practices

Establish a comprehensive logging system to record:
- Detailed application operations, data manipulations, errors, and informational messages.
- Differentiate log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- Dynamic logging configuration through environment variables for levels and output destinations.


### Design Patterns for Scalable Architecture

Incorporate key design patterns to address software design challenges, including:
- **Facade Pattern:** Offer a simplified interface for complex Pandas data manipulations.
- **Command Pattern:** Structure commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns:** Further enhance the application's code structure, flexibility, and scalability.



