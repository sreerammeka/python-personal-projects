# Object Oriented Programming (OOPS) in Python

# Object- An instance of the class (design) is called an Object

# Class- A design of an Object is called Class

# Encapsulation
# Abstraction
# Polymorphism

# Classes and Objects
# In Python, everything created are Objects

# Built in data types such as integer, string, float are classes which are inbuilt classes
# All the bultin datatypes and builtin functionality is stored in builtins.py
# If we want to create a new type, we can create a class like below
# Creating a class
class computer:
    # Inside a class, we define attributes (which is done using Variables), behavior (which is done using methods or functions)
    def config(self):
        print("The computer configuration is i7, 16GB RAM, 1TB")


# Creating an "Object" com1 from a "Class" Computer
com1 = computer()
com2 = computer()

# Checking the data type of com1 and com2, outputs as "class module_name.class_name"
print(type(com1))
print(type(com2))

# In order to access the function inside a class, we can do so below
# Syntax is class_name.function_name(object_name)
# We need to specify the object_name as we will have thousand Objects
computer.config(com1)

# We can also use the object and then call the function or method
# Since com1 will reference the "computer" class, and also we don't need to pass an Object name as we are using the object_name to reference the class
# In regular usage, we will see the usage more frequently
com2.config()

# Here, we are automatically passing "a" to the bit_length method without specifying in the brackets, since "a" is considered an Object by Python
a =5
a.bit_length()