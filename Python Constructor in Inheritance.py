# Example to showcase how a Constructor works with Inheritance Concept
# We are also using same feature names in different classes to check how it works
# Method Resolution Order (MRO): If we use Multiple Inheritance, which uses multiple Super Classes, then the first superclass will be printed for __init__ method.
# We can call the superclass using "super.__init__()"


class A:
    # Constructor
    def __init__(self):
        print("This is from Class A Init")

    def feature1(self):
        print("Feature 1A is working")

    def feature2(self):
        print("Feature 2A is working")


# Note: If Class B inherits from Class A, and if Class B doesn't have its own constructor __init__ method and Class A has the constructor __init__ method, then it will execute the functionality mentioned in __init__ method of Class A
# If Class B inherits from Class A, and if Class B has its own constructor __init__ method and Class A ALSO has its own constructor __init__ method, then it will execute the functionality mentioned in __init__ method of Class B and NOT from Class A
class B:
    # Constructor
    def __init__(self):
        print("This is from Class B Init")

    def feature1(self):
        print("Feature 1B is working")

    def feature2(self):
        print("Feature 2B is working")


# Multiple Inheritance
class C(A, B):
    # Constructor
    def __init__(self):
        # We can use the super method to print the superclass A, which uses MRO concept described above
        # Calls the __init__ method of the Superclass A and NOT B even though there were two Superclasses A and B
        #
        # super(C, self).__init__
        super().__init__()
        print("This is from Class C Init")

    def feature1(self):
        print("Feature 1C is working")

    def feature2(self):
        print("Feature 2C is working")

    def feat(self):
        # Here Super method refers to Superclass A, and feature 2 functionality will be executed
        super().feature2()


# Creating Objects for Classes A, B, C
# If the Objects a and b are not created, and ONLY object c is created then, it will execute __init__ method of Class C, even though Class A and Class B are Superclasses
a = A()
b = B()
c = C()

# Below will execute functionality of feature 2 from Superclass A, because feature 2 and superclass method is called in feat() function in Class C
c.feat()
