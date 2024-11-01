import logging

logger = logging.getLogger('root')

def show_history(history):
    """Print the history of commands executed."""
    print("\nCalculation History:")
    for index, (command, args, result) in enumerate(history, 1):
        print(f"{index}. {command.capitalize()}({', '.join(map(str, args))}) = {result}")
    print()

def clear_history(history):
    """Clear the calculation history."""
    history.clear()
    logger.info("Calculation history cleared.")
    print("History cleared.\n")
