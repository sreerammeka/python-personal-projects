# Different Types of Methods
# 1. Instance Methods- Whenever we want to instantiate variables (use instance variables), use the Instance Method
# 2. Class Methods (@classmethod)- Whenever we want to work with class variables, we use the Class Method
# 3. Static Methods (@staticmethod)- Whenever we want to print something (which is static or doesn't change) or use methods of classes from other modules, we use the Static Method??
# **If we are working with instance variables, we have to use "self" keyword, whereas if we are working with class variables we have to use "cls" keyword

# # Car class still in draft
# class car:
#     # The variables used outside of instance methods and inside a class is called "Class Methods"
#     # Class variables are below, if changed anywhere in the Class will apply throughout the Class
#     wheels = 4
#
#     def __init__(self):
#         # Instance variables are below, they are not changed
#         # The Methods used to instantiate instance variables are called "Instance Methods"
#         self.car_name = "Honda"
#         self.car_model = "Accord"
#         self.car_year = 2020
#         self.starting_price = 25000
#
#
#     def car_renewal(self):
#         self.car_lease_time_in_yrs = 2


class Student:

    # school_name is a class variable
    school_name = "Gordon University"

    # __init__ method used to initialize variables
    # m1, m2, m3 are instance variables, since we are using "self" keyword which is used with instance variables
    def __init__(self, m1, m2, m3):
        # m1, m2 and m3 are marks we are taking from the user
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Whenever we call s1.avg(), then it maps "s1" Object to "self" Object returns (s1.m1 + s1.m2 + s1.m3)/3
    # avg() is an instance method since it works with the Object "self"
    # ***Instance Method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # ***Class Method
    # Let's say we want to get school_name, which is a Class variable, we have to use the Class method
    @classmethod
    def school_info(cls):
        return cls.school_name

    # ***Static method
    # If we don't want to use instance variables or class variables, then we will use static methods
    # We don't need to pass any arguments like "self" or "cls" for static methods
    # Normally
    @staticmethod
    def school_type():
        print("Gordon University is a Public University")

    # If we have variables, we have two different types of methods
    # 1. Accessor Methods (to access data. i.e using get)
    # 2. Mutuator Methods (to modify data. i.e using set)
    # Examples are below
    # 1. Accessor Method Example

    # def get_marks(self):
    #     return self.m1, self.m2, self.m3

    # method to get marks m1 (i.e same subject) of ALL students when called by s1.get_m1 and s2.get_m1
    def get_m1(self):
        return self.m1

    # Mutuator Method Example
    def set_m1(self, value):
        self.m1 = value


s1 = Student(23, 34, 56)
s2 = Student(54, 36, 57)

# If we want to access individual marks, we can do so below using the "Object" s1 and s2
print(s1.m1, s1.m2, s1.m3)
print(s2.m1, s2.m2, s2.m3)

# If we want to get the average of marks obtained by a Student, call the s1 Object and call the avg method by s1.avg()
print(s1.avg())
print(s2.avg())

# We can print the school name by using Objects s1 and s2 but since for all the students, school name is same, we should reference the class name and get/access the variable name
print(s1.school_name)
print(s2.school_name)

# The school name can be accessed using the class name, like below instead of s1.school_name or s2.school_name
print(Student.school_name)

# If we don't use @classmethod before the school_info method, then a TypeError will occur saying "cls" has to be passed as an argument
print("School name is: ", Student.school_info())

# If we try to print Student.get_m1, it doesn't know which student we are talking about, so only prints "class_name.method_name and address
print(Student.get_m1)

# Set or Change the value of m1 from 23 to 45 by calling the set_m1 method
s1.set_m1(45)

# prints marks of student S1 by calling the get_m1 method
# It has to print 23 but we are changing the value using the set_m1 method which changes s1.m1 to 45
print(s1.get_m1())

# There is no need to use the print function below as the school_type method already has a print function
Student.school_type()



