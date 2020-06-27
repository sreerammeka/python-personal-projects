# Decorators in Python
# Python Decorators are almost similar to annotations in Java

# If the value of a is less than b, then swap values, and then perform division
# If the value of a is greater than b, then perform division

def div(a, b):
    print(a / b)


# We are passing a function "func" inside a function "smart_div"
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        # func(a,b) calls div(a,b) since "div" is passed as an argument to smart_div function
        return func(a, b)
    # Returns the return value of "inner" function, which is func(a,b) => which is actually div(a,b)
    return inner

# div1 is like a new function, where we are passing "div" as an argument which gets mapped to "func" in smart_div function
div1 = smart_div(div)

div1(2, 4)
