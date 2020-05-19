# Matrix multiplication
from numpy import *

arr1 = array([1, 2, 3], int)
arr2 = array([3, 3, 9], int)
arr3 = array([2, 3, 4], int)

# Creating a 2D arrays from two 1D arrays
arr4 = array([arr1, arr2, arr3], int)

# Multiply each element in one 1D array with each element in other 1D array
arr5 = arr4 * arr4
print("arr1 is: ", arr1)
print("arr2 is: ", arr2)
print("arr3 is: ", arr3)
print("arr4 is: ", arr4)
print("arr5 is: ", arr5)