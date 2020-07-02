# Functions are used to perform smaller tasks and are used to reuse the functionality without defining
# the function again and again

# Python has in-built functions which are developed by the Python Community
# and user defined functions to perform specific tasks

# math functions
# To use it , import math module for performing sqrt, floor, ceil, factorial, sin, cos, power, pi, epsilon (e)

import math

# a = math.floor(2.9) returns 2
a = math.floor(2.9)
# b = math.ceil(2.9) returns 3
b = math.ceil(2.9)
# p = math.floor(2.1) returns 2
p = math.floor(2.1)
# q = math.ceil(2.1) returns 3
q = math.ceil(2.1)

# Power function
# math.pow(3,2) returns 3**2 i.e 9 as output

# Instead of importing entire library, we can import functions that are used by below. We can call pow directly instead of pow(3,2) instead of math.pow(3,2)
from math import sqrt, pow

# To find the functions in a module
# help('math') or help("math")

print(a, b, p, q)
