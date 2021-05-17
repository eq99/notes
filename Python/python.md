- https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial#toc-1



## How __init__ and __main__ work

Names that start and end with double underscores, often called 'dunders', are special names in Python. Two of them are special names related to modules and packages: `__init__` and `__main__`. Depending on whether you are organizing your code as a package or a module, they are treated slightly differently.

We will look at the difference between a module and a package in a moment, but the main idea is this:

- When you import a package it runs the `__init__.py` file inside the package directory.
- When you execute a package (e.g. `python -m my_package`) it executes the `__main__.py` file.
- When you import a module it runs the entire file from top to bottom.
- When you execute a module ir runs the entire file from top-to-bottom *and* sets the `__name__` variable to the string `"__main__"`.

