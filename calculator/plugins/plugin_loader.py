import os
import importlib
import logging

logger = logging.getLogger('root')

def load_plugins(commands):
    plugin_dir = 'calculator.commands'
    plugin_path = plugin_dir.replace('.', '/')
    
    try:
        for plugin_name in os.listdir(plugin_path):
            if plugin_name.endswith('_command.py') and plugin_name != '__init__.py':
                try:
                    # Derive module and class name
                    module_name = f"{plugin_dir}.{plugin_name[:-3]}"
                    class_name = plugin_name.split('_')[0].capitalize() + "_Command"
                    
                    # Import module and class
                    module = importlib.import_module(module_name)
                    command_class = getattr(module, class_name)
                    
                    # Register command
                    command_name = plugin_name.split('_')[0]
                    commands[command_name] = command_class()
                    logger.info(f"Loaded plugin: {command_name}")

                except AttributeError:
                    logger.error(f"Class '{class_name}' not found in module '{module_name}'. Skipping plugin.")
                except Exception as plugin_error:
                    logger.error(f"Failed to load plugin '{plugin_name}': {plugin_error}")

    except FileNotFoundError:
        logger.error(f"Plugin directory '{plugin_path}' not found.")
    except Exception as e:
        logger.error(f"Failed to load plugins: {e}")
