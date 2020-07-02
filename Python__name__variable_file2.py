# Python example about what happens when importing a module and check what prints if __main__ is mentioned in the imported module
# Need to import sys only if sys.path is to be used
import sys

# Need to check how we can import modules with spaces in the module file name, temporarily removed spaces to test __name__ functionality

# Importing a user written module into other file/module
# Syntax is
# from module_name import all_modules_or_custom_functions
# If we import all functions from other modules, then the entire imported module will be executed first
# NEED TO TEST WHAT HAPPENS IF SPECIFIC FUNCTIONS ARE IMPORTED

from Python__name__variable import func1

# When we execute this module/file, then __name__ will print __main__
# If __name__ is present in a different module, then that module/file name will be printed instead of __main__
print("Hello" + __name__)

# To append or add a path, we can use sys.path
# sys.path.append("Python__name__variable.py")
# print(sys.path)
# sys.path.append("python-personal-projects\Python__name__variable.py")
