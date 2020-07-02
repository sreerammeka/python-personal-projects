# Python example about what happens when importing a module and check what prints if __main__ is mentioned in the imported module
# Need to import sys only if sys.path is to be used
import sys
from Python__name__variable import *
# Need to import the importlib to also import a module without using "import" or "from...import"
import importlib


# Importing a user written module into other file/module
# Syntax is
# from module_name import all_modules_or_custom_functions

# If we import all functions from other modules, then the entire imported module will be executed first
# NEED TO TEST WHAT HAPPENS IF SPECIFIC FUNCTIONS ARE IMPORTED

# ***If we want import a module with spaces in module name, then use __import__("module_name")
# ***It is recommended to NOT use spaces in module names/file names, as it will be difficult to access functions, methods, classes etc
# __import__("Python Functions")

# from Python Functions import *

# We can also use the importlib library and use the import_module function to import modules (with spaces)
importlib.import_module("Python Functions")



# When we execute this module/file, then __name__ will print __main__
# If __name__ is present in a different module, then that module/file name will be printed instead of __main__
print("Hello" + __name__)

# To append or add a path, we can use sys.path
# sys.path.append("Python__name__variable.py")
# print(sys.path)
# sys.path.append("python-personal-projects\Python__name__variable.py")
