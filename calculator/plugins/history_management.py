import logging

logger = logging.getLogger('root')

def show_history(history):
    if not history:
        print("Sorry! No history available.")
        logger.info("Attempted to show history but no history available.")
        return

    print("\nCalculation History:")
    for index, (command, args, result) in enumerate(history, start=1):
        print(f"{index}. {command.capitalize()}({', '.join(map(str, args))}) = {result}")
    logger.info("Displayed calculation history.")
    print()

def clear_history(history):
    history.clear()
    logger.info("Calculation history cleared.")
    print("History cleared.\n")

def save_entry(history, command: str, args: tuple, result):
    entry = (command, args, result) 
    history.append(entry)  
    logger.info(f"Saved entry: {entry}") 