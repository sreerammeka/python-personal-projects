# User defined functions
# Note: Even if functions are called, they won't print anything without the print statement.
# Functions just returns and store values but not output it unless you print them

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
    return c,d,e,f,g

print("The addition and subtraction of two numbers is:", add_sub(3, 4))

# Storing or assigning the function return values to a variable
result = add_sub(5,6)
print(result)



