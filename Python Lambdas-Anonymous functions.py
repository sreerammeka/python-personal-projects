# Lambdas are anonymous functions without a name
# Lambdas can be declared on a single line
# Lambdas can operations similar to functions and these can be passed to other functions
# Syntax is below
# lambda input_arguments: output_expression
# Only one output_expression can be evaluated unlike functions where multiple operations can be performed inside a function
# lambdas don't print anything by default, similar to a function
# Lambdas can be used instead of functions

# Input argument is "a" and outputs a * a to f1, f1 works like a function
f1 = lambda a: a * a
# We have two input arguments a and b, performs the operation a+b and returns the value to f2, where f2 works like a function
f2 = lambda a,b: a+b

# f1 works like a function and passes 5 to a and returns 5 * 5 which is 25
result1 = f1(5)

# We are passing two arguments 4 to a and 7 to b and stores the output value to result2
result2 = f2(4,7)
print(result1)
print(result2)
