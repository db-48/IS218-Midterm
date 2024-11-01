import os
import importlib
import logging

logger = logging.getLogger('root')

def load_plugins(commands):
    plugin_module_name = 'calculator.plugins.commands'  

    try:
        module = importlib.import_module(plugin_module_name)
        
    
        for attribute_name in dir(module):
            if attribute_name.endswith('_Command'):
                command_class = getattr(module, attribute_name)
                if callable(command_class): 
                    command_name = attribute_name[:-7].lower()  
                    commands[command_name] = command_class()
                    logger.info(f"Loaded plugin: {command_name}")

    except ImportError:
        logger.error(f"Plugin module '{plugin_module_name}' not found.")
    except Exception as e:
        logger.error(f"Failed to load plugins: {e}")

