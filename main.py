import os


def load_module(module_name):
    '''
    Dynamically loads modules from plugins folder based on module name.
    '''
    name = f'plugins.{module_name}'
    mod = __import__(name, fromlist=[''])

    if mod and hasattr(mod, 'call'):
        return mod
    
    return None


def get_plugins():
    '''
    Returns a list of module names from plugins folder without file extension.

    Any Python file other than __init__.py in plugins/ folder is considered a plugin
    '''
    plugins = []
    for _, _, files in os.walk('plugins'):
        for f in files:
            if f.endswith('.py') and f != '__init__.py':
                base = os.path.basename(f)
                fname = os.path.splitext(base)[0]
                plugins.append(fname)
    return plugins


for plugin in get_plugins():
    print(f'Loading plugin {plugin}')
    mod = load_module(plugin)
    print(mod.call()[:5])
