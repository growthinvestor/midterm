import os
import importlib

PLUGINS = {}

def load_plugins():
    plugins_path = os.path.dirname(__file__)
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"calculator.plugins.{module_name}")
            if hasattr(module, "register_plugin"):
                PLUGINS.update(module.register_plugin())

def get_plugin(plugin_name):
    return PLUGINS.get(plugin_name)
