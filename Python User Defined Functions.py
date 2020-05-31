# User defined functions
# Note: Even if functions are called, they won't print anything without the print statement.
# Functions just returns and store values but not output it unless you print them
# The number of input arguments passed when defining a function must be passed when calling the function,
# Otherwise, it will throw an error

# Function Syntax
# def function_name(arguments or values to pass):
#     <code logic>

# Calling a function:
# Call the function and if the function has NO arguments or values to pass:
# Syntax is:
# function_name()

# Call the function and if the function has arguments or values to pass:
# Syntax is:
# function_name(arguments to pass)

# User defined add function
def add(x, y):
    c = x + y
    # Returns "None" if return statement is not mentioned
    # return c
    # Instead of returning c, just print c
    print(c)


# Values 5 is passed to x and 7 is passed to y and the operation inside the add function is performed
# add(5, 7)
# Values 4 is passed to x and 3 is passed to y and the operation inside the add function is performed
# add(4, 3)

def add_sub(x, y):
    # We can perform multiple tasks in the same function
    # Here both addition and subtraction is performed in the same function
    c = x + y
    d = x - y
    e = x * y
    f = x / y
    g = x % y
    # We can also return any number of values c, d, e, f, g
    # If we are not returning anything then we are just storing it or performing some operation but it won't return anything
    return c, d, e, f, g


print("The various operations on two numbers is:", add_sub(3, 4))

# Storing or assigning the function return values to a variable
result = add_sub(5, 6)
print("The values stored in result is:", result)

# Printing the type of "result"
print(type(result))

# We can also store return values separately in different variables by:
# Stores c in result1 and d in result2
result1, result2, result3, result4, result5 = add_sub(5, 6)

print("The values in result1...result5 is: ", result1, result2, result3, result4, result5)


# *** Pass By Value and Pass By Reference in Python
# Note: In Python, we don't have the concept of 'pass by value' or 'pass by reference'. Instead, we have immutable or
# mutable arguments passed to the function. If we pass immutable objects like integer or string to function and try to
# update their value, their original value will not be updated instead a new variable will be created with updated
# at new memory address. If we pass mutable objects like list or dictionary and try to update them, their original value
# will be updated at the same memory address.

# A list can also be passed as inputs arguments to a function

def list_func(list1):
    print(id(list1))


list1 = [2, 0, 43]
print(id(list1))
# list1[]

list1.sort()
print(list1)

list1.reverse()
print(list1)


# Additional examples with different arguments
# Immutable object as argument - Integer, String

def update(x):
    print('Value of x ', x)
    print('Memory Address of x before update', id(x))
    x = 8
    print('Value of x after update', x)
    print('Memory Address of x after update', id(x))


a = 10
print('Value of a ', a)
print('Memory Address of a before update', id(a))
update(a)
print('Value of a ', a)
print('Memory Address of a before update', id(a))


# Mutable object as argument - List

def update(x):
    print('inside function, before update', spam)
    print('Memory address of list inside function, before update', id(spam))
    spam[1] = -3
    print('inside function, after update', spam)
    print('Memory address of list inside function, after update', id(spam))


spam = [1, 2, 3]
print('Items in list', spam)
print('Memory address of list', id(spam))
update(spam)
print('Items in updated list', spam)
print('Memory Address of updated list', id(spam))
