import logging
import pandas as pd

logger = logging.getLogger('root')


def show_history(history_data):
    if history_data.empty:
        print("Sorry! No history available.")
        logger.info("Attempted to show history but no history available.")
        return

    print("\nCalculation History:")
    for index, row in history_data.iterrows():
        command = row['command_name'].capitalize()
        args = row['args']
        result = row['result']
        print(f"{index + 1}. {command}({', '.join(map(str, args))}) = {result}")
    logger.info("Displayed calculation history.")
    print()

def clear_history(history_data):
    return pd.DataFrame(columns=['command_name', 'args', 'result'])

def save_entry(history_data, command: str, args: list, result):
    entry = pd.DataFrame({'command_name': [command], 'args': [args], 'result': [result]})
    updated_history_data = pd.concat([history_data, entry], ignore_index=True)
    logger.info(f"Saved entry: {entry.to_dict(orient='records')[0]}")
    return updated_history_data