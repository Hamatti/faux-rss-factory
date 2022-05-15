import os
from settings import INSTALLED_PLUGINS


def load_module(module_name):
    '''
    Dynamically loads modules from plugins folder based on module name.
    '''
    name = f'plugins.{module_name}'
    mod = __import__(name, fromlist=[''])

    if mod and hasattr(mod, 'call'):
        return mod
    
    return None


for plugin in INSTALLED_PLUGINS:
    print(f'Loading plugin {plugin}')
    mod = load_module(plugin)
    print(mod.call()[:5])
