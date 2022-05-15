# Plugins

Here will be documentation of how to implement a plugin for each blog

## Plugin Architecture

Each plugin needs to adhere to three rules:

1. It must implement `call` function with no parameters
2. The `call` function must return a list of blog posts as dictionaries
3. The module filename cannot contain `-`, `_`, `.` or other special characters

Plugins may then have more private functions that take care of fetching, parsing and cleaning the data.

## Installing a plugin

Once you have created a plugin file, add the name of the plugin (without `.py` extension) in `settings.py`'s `INSTALLED_PLUGINS` list.

## Example

See `hamattiorg.py` for an example of parsing my personal blog at [https://hamatti.org/blog](https://hamatti.org/blog). It does provide RSS so you don't need this tool for it but it's easier to keep as an example since I control its changes.
