# Examples and usages of the __init__ method
# By default, __init__ method gets executed even though it is not called
# If there are "n" Objects, __init__ method gets executed "n" times, even though it is NOT called
# Normally, we use the __init__ method to initialize variables or data
# __init__ method is a special method similar to __name__ special variable
# __init__ method gets executed first even though __init__ method is mentioned at the end of the class

class computer:
    # Inside a class, we define attributes (which is done using Variables), behavior (which is done using methods or functions)
    # What I can observe is, we are using the "self" Object to access the local variables from the __init__ method without using the "global" keyword
    def config(self):
        print("The computer configuration is: ", self.cpu_power, self.ram_memory)

    def __init__(self, cpu, ram):
        # We need to call the "self" Object first to assign variables or data such as cpu and ram
        self.cpu_power = cpu
        self.ram_memory = ram
        self.name = "John"
        self.age = 28
        print(self.cpu_power, self.ram_memory)


# "com1" is passed as an Object automatically and maps to the "self" Object in __init__ method, and i7 as CPU and 16 as ram
# Lets say we want to pass cpu configuration as i7 and RAM as 16 GB
# Whenever we execute the program, a new object will be created with a different address even though com1 and com2 are referencing to the same Class
# These Objects are stored in memory called "Heap memory"
# Who determines the size of the Object? Constructor
# Here Constructor is computer(), determines the size of the Object
com1 = computer("i7", 16)
com2 = computer("AMD", 8)

# We are changing the value of the variables by calling the Objects com1 and com2 which is mapping to "self" Object.
com1.name = "Chris"
com2.age = 34

print(com1.name)
print(com1.age)
print(com2.name)
print(com2.age)
# This below object is only needed when we want to execute the config() method
# By default, ALL the __init__ methods will be executed first, when multiple Objects have been created
com1.config()
com2.config()
