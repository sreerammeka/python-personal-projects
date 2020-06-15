# Global and local variables
# Scope

# global variable can be used anywhere throughout the program, even inside a function if it's not changed
a = 10
b = 17
c = 18

def func1():
    # local variable
    global a
    a = 15
    # To use b value outside this function, define it as "global b"
    global b
    b = 12
    # Will print 15 if the local variable has changed from 10 to 15
    print("inside function is", a)

func1()

# Error is Unresolved Reference because b is defined inside a function, and b is a local variable which can't be used
# outside the function
# In order to use a local variable outside the function,

print("the value of b is", b)

# Will print 10 since the global value of a is 10
print("outside function is", a)

# We want to have a local variable and also change the value of a global variable
def func2():
    # Access all the Global variables
    x = globals()
    print("The global variables are", x)
    # In order to access a specific global variable, say globals()[a]
    x = globals()['a']
    # Will print 15 since we made "a" as global in func1
    print("The global variable a accessed through x is", x)
    # x will have same memory location as a, as it has the same value when referenced as
    print(id(x))
    # Changing the value of a global variable through access without effecting the local variable
    globals()['a'] = 20


print(id(a))
func2()

