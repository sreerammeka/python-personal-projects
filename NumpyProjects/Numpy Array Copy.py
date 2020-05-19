# Copying an array into another array using Numpy

from numpy import *

arr1 = array([2, 4, 8, 6], int)
arr2 = array([3, 5, 2, 4], int)
# Adding two arrays will add each element in one array with each element in the other array
# Here zeroth elements 2 and 3 gets added and results to 5, 4 and 5 gets added and results to 9, 8 and 2 gets added and results to 10, 6 and 4 gets added and results to 10
arr3 = arr1 + arr2
print("The sum of two arrays arr1 and arr2 is: ", arr3)

# Sum of elements in an array
# Final output sum should return 20
sum_array =0
for i in range(len(arr1)):
    sum_array = arr1[i] + sum_array
    # break out of loop if the last element is reached, i.e if i exceeds the maximum length of the array, then break out of the loop
    if i > len(arr1):
        break

print("The Sum of ALL elements in an array arr1 is: ", sum_array)

# Trigonometric operations using Numpy
# Sine operation
print(sin(arr1))

# Cosine operation
print(cos(arr1))

# Tan operation
print(tan(arr1))
