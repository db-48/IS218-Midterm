import os
import importlib
import logging

logger = logging.getLogger('root')

def load_plugins(commands):
    """Dynamically load additional plugins if they follow a naming convention."""
    plugin_dir = 'calculator.commands'
    try:
        for plugin_name in os.listdir(plugin_dir.replace('.', '/')):
            if plugin_name.endswith('_command.py') and plugin_name != '__init__.py':
                module_name = f"{plugin_dir}.{plugin_name[:-3]}"
                module = importlib.import_module(module_name)
                command_class = getattr(module, plugin_name.split('_')[0].capitalize() + "_Command")
                command_name = plugin_name.split('_')[0]
                commands[command_name] = command_class()
                logger.info(f"Loaded plugin: {command_name}")
    except Exception as e:
        logger.error(f"Failed to load plugins: {e}")
