# Polymorphism
# Poly means many and morph means forms -> many forms
# Types of Polymorphism
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding
# Other concepts such as Loose Coupling, Dependency Injection, Interface

# 1. Duck Typing Example

class developer_tools:
    def execute(self):
        print("Compiling Code")
        print("Executing Code")


class Laptop:

    # Here "ide" is an argument, which passes an Object for the class "tool", since "ide_tool" maps to "ide"
    # "ide_tool" points to the Object for the class "developer_tools" and executes the "execute()" method inside "developer_tools" class
    # For this to execute, "execute()" method should exist inside the "developer_tools" class, otherwise it will throw an error
    def code(self, ide):
        ide.execute()


lap1 = Laptop()
ide_tool = developer_tools()

# "ide_tool" Object is passed as
lap1.code(ide_tool)
