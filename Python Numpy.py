# Numpy examples
# Numpy can be used for multi-dimensional arrays such as matrix which is two dimensional, dice which is three-dimensional etc.
# We can also use

# Using the Numpy module
# If module not found, then install the module from IDE
from numpy import *

# One dimensional array using Numpy
arr1 = array([2,3,4,5,6], int)
print(arr1)

# Different ways of creating an array
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()

# array()
# One dimensional integer array using Numpy
# arr1 = array([2,3,4,5,6], int)
# One dimensional float array using Numpy
arr1 = array([2,3,4,5,6], float)
print("The value of array arr1 is: ", arr1)

# linspace()
# linspace is used to divide into parts and the return value is float, by default if not mentioned will divide into 50 parts
# linspace syntax is linspace(starting_value, ending_value, parts_to_divide)
# linspace takes ending value unlike range() which excludes ending value mentioned in range()
# Here start from 0 and end with 16 and divide the values between 0 and 16 by 50 parts
arr2 = linspace(0,16,50)
print("The value of array arr2 is: ", arr2)

# logspace()
# logspace will return the values from 10^starting_value to 10^(ending_value) with number of parts to divide, here 5 parts
arr3 = logspace(1,40,5)
print("The value of array arr3 is: ", arr3)
# %.2f means value till 3 float digits
print("The first value in array arr3 up to three float digits is: ", '%.3f' % arr3[0])

# arange()
# arange is similar to range() but only available in Numpy library
# Start with 1 and end with 15 since this is range and step is 2
arr4 = arange(1,16,2)
print("The value of array arr4 is: ", arr4)

# zeros()
# zeros() will return ALL zeros with float values by default, we can also convert them to an integer
arr5 = zeros(5, int)
print(arr5)

# ones()
# ones() will return ALL ones with float values by default, we can also convert them to an integer
arr6 = ones(5, int)
print(arr6)