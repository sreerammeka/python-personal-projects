# Example to define classes within classes (Inner Class)
# Note: You can create an Object for Inner Class inside/within the Outer Class OR you can also create an Object for Inner Class Outside Outer Class by calling the Student.Courses() or Student.Courses.Laptop()

class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.studentid = student_id
        # self.Courses = self.Courses()
        # Below, we are creating an Object for inner class "Courses" here
        # self.courses_available = self.Courses()

        # We are creating an Object for inner class "Courses" here and passing the value "Physics" to the argument "course_name" and the value "FALLBA126" to argument "course_id" below
        self.courses_available = self.Courses("Physics", "FALLBA126")


    class Courses:

        def __init__(self, course_name, course_id):
            # self.course_name = "Physics"
            # self.course_id = "FALLBA126"
            # If we want to pass values through user input
            self.course_name = course_name
            self.course_id = course_id
            # Creating an Object for the Inner Class "Laptop" within the "Courses" Inner Class
            self.laptop_brand = self.Laptop("HP", "8GB", "500GB")

        # @staticmethod
        def show_courses(self):
            print("The courses the student enrolled are: ", self.course_name, self.course_id)
            return self.course_name, self.course_id

        # Creating another Inner Class "Laptop" inside "Courses" Inner Class
        class Laptop:

            def __init__(self, brand, ram, hard_drive):
                self.brand_name = brand
                self.ram_memory = ram
                self.hard_drive_space = hard_drive

            def show_laptops(self):
                print(self.brand_name, self.ram_memory, self.hard_drive_space)


s1 = Student("John", "CSE67890")

# If we want to access variables in an inner class, i.e class within a class, then we have to use the outer class first, then access the inner class and the inner class variables
# We can't directly access the inner class variables by calling the outer class Object
print(s1.courses_available.course_name, s1.courses_available.course_id)

print(s1.courses_available.show_courses())

# print(s1.laptop_brand.show_laptops)

# In order to access an Inner Class within an Inner Class, create an Object for "Laptop" Class within the Inner Class "Courses"
print(s1.courses_available.laptop_brand.show_laptops())

# Note: We can also create an Object for Inner Class outside the Outer Class if its not created inside/within the Outer Class
# Creating an Object for Inner Class outside the Outer Class
course1 = Student.Courses("Math", "SPRNBA349")

print(course1.show_courses())
