# Example to define classes within classes (Inner Class)

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

        # @staticmethod
        def show_courses(self):
            print("The courses the student enrolled are: ", self.course_name, self.course_id)
            return self.course_name, self.course_id


s1 = Student("John", "CSE67890")

# If we want to access variables in an inner class, i.e class within a class, then we have to use the outer class first, then access the inner class and the inner class variables
# We can't directly access the inner class variables by calling the outer class Object
print(s1.courses_available.course_name, s1.courses_available.course_id)

print(s1.courses_available.show_courses())
