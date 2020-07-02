# Decorators in Python
# Python Decorators are almost similar to annotations in Java
# Decorators are used to add additional functionality without modifying the original function

# If the value of a is less than b, then swap values, and then perform division
# If the value of a is greater than b, then perform division


# We are passing a function "func" inside a function "smart_div"
# We are adding additional functionality using smart_div
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        # func(a,b) calls div(a,b) since "div" is passed as an argument to smart_div function
        return func(a, b)

    # Returns the return value of "inner" function, which is func(a,b) => which is actually div(a,b)
    return inner


# div1 is like a new function, where we are passing "div" as an argument which gets mapped to "func" in smart_div function
# Instead of below, we can just use the added functionality smart_div using @smart_div before "div" function
# "smart_div" must be declared before "div" function because "div" function is using this functionality
# div1 = smart_div(div)

@smart_div
def div(a, b):
    print(a / b)


div(2, 4)
