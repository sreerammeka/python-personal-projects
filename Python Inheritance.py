# Inheritance
# Child Class Inherits the features of the Parent Class (or Sub Class Inherits the features of the Super Class)

# Suppose if we have a Parent Class "A" and a Child Class "B" and if we want Class "B" to use features of Class "A" without redefining the features of Class "A" inside Class "B", then we can use the concept of Inheritance where Class "B" can use featues of Class "A"

# Single level Inheritance
# If Only Class "B" Inherits from a single class Class "A", then it is called Single level Inheritance
# Syntax is below
# class B(A)

# Multi level Inheritance
# If Class "C" Inherits from the class Class "B", which inturn inherits Class "A, then it is called Multi level Inheritance
# Syntax is below
# class C(B)
# Above class C(B) will inherit from both Class "B" as well as Class "A", since Class "B" also inherits from Class "A"

# Multiple Inheritance
# Inheriting a class from multiple classes is called Multiple Inheritance
# Syntax is below
# class D(A, P)
# Above class D(A, P) will inherit from both Class "A" as well as Class "P" at the same time

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


# If we want Class "B" to inherit Class "A", then use Class "A" as an argument for Class B"
# Syntax is below
# class B(A):

# Applying Inheritance, Class "B" inherits from Class "A"
class B(A):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


# Applying Multi Level Inheritance, Class "C" inherits from Class "B" as well as Class "A"
class C(B):
    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")


class P:
    def feature7(self):
        print("Feature 7 is working")

    def feature8(self):
        print("Feature 8 is working")


# Multiple Inheritance Example
# Inheriting a class "D" from multiple classes "A" and "P" which are not inherited by any other classes, is an example of Multiple Inheritance
class D(A, P):
    def feature9(self):
        print("Feature 9 is working")

    def feature10(self):
        print("Feature 10 is working")


# Creating Object A
a1 = A()
# Creating Object B
b1 = B()
# Creating Object C
c1 = C()
# Creating Object P
p1 = P()
# Creating Object D
d1 = D()

print("Printing Features of Class A")
# a1 Object can ONLY access the features of Class "A", , i.e features 1 and 2
a1.feature1()
a1.feature2()

print("Printing Features of Class B without Inheritance")
# Without Inheritance, b1 Object can ONLY access the features of Class "B", i.e features 3 and 4
b1.feature3()
b1.feature4()

print("Printing Features of Class A using Class B by using Single Level Inheritance")
# With Inheritance, b1 Object can ALSO access the features of Class "A" as well as its own features of Class "B", i.e features 1, 2, 3 and 4
b1.feature1()
b1.feature2()

print("Printing Features of Class C using Class B (and Class A) by using Multi Level Inheritance")
# With Multi Level Inheritance, c1 Object can ALSO access the features of Class "B" and Class "A" as well its own features of Class "C", i.e features 1, 2, 3, 4, 5 and 6
# Notice below c1 Object can use features 1 and 2 from Class A and features 3 and 4 from Class B as well as its own features of Class "C", i.e features 5 and 6
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

print("Printing Features of Class D using Single Classes Class A and Class P by using Multiple Inheritance")
# With Multiple Inheritance, d1 Object can Inherit features from both Classes "A" and "P" at the same time
# Class A has features 1 and 2 and Class "P" has features 7 and 8, Class D has features 9 and 10
d1.feature1()
d1.feature2()
d1.feature7()
d1.feature8()
d1.feature9()
d1.feature10()
