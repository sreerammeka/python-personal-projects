# Copying an array into another array using Numpy and performing some functions on an array

from numpy import *

arr1 = array([2, 4, 8, 6], int)
arr2 = array([3, 5, 2, 4], int)
# Adding two arrays will add each element in one array with each element in the other array
# Here zeroth elements 2 and 3 gets added and results to 5, 4 and 5 gets added and results to 9, 8 and 2 gets added and results to 10, 6 and 4 gets added and results to 10
arr3 = arr1 + arr2
print("array arr1 is: ", arr1)
print("array arr2 is: ", arr2)
print("The sum of two arrays arr1 and arr2 is: ", arr3)

# Note: In Python, copying an array or value will point to the same address location.
# i.e if two variables or arrays are same, then they will point to the same address location
# If we want to change the memory address location for same values use the "view" method

# Copying an existing array arr1 to a new array arr4
arr4 = array(arr1)
print("array arr4 after copying is: ", arr4)
# Copying an existing array arr1 to a new array arr5 by directly assigning arr1 to arr5
arr5 = arr1
print("array arr4 after copying by direct assignment is: ", arr5)

# Copy values from one array to the other with different memory locations
# Use view() method, view() method creates a new array and stores both arrays in different memory address locations
# view uses "Shallow Copy", which means even if the value of any element in arr1 is changed,
# then the value in arr6 will be changed irrespective of altering the value anywhere in the program

# Below arr6[1]= 5 even though we changed the value of arr1[1] = 5 after copying it.
arr6 = arr1.view()
arr1[1] = 5
print("array arr6 after copying using view method is: ", arr6)

# Concatenate two arrays arr1 and arr2
print("The concatenated array of arrays arr1 and arr2 is: ", concatenate([arr1, arr2]))

# Deep Copy
# We use the copy() method for Deep Copy
# Deep Copy will copy elements or values from one array to the other array with different memory locations
# Even if the previous array is altered after copying, still the new array values will store the previous values
# at different memory address locations
# We use the copy() method for Deep Copy

arr7 = arr1.copy()
arr1[1] = 5
print("array arr7 after copying using view method is: ", arr7)

# Sum of elements in an array
# Final output sum should return 20
sum_array = 0
# Iterate till the length i.e number of elements in the array arr1
for i in range(len(arr1)):
    # Add sum_array by indexing each value in iteration and storing the previous result in sum_array
    sum_array = arr1[i] + sum_array
    # break out of loop if the last element is reached, i.e if i exceeds the maximum length of the array, then break out of the loop
    if i > len(arr1):
        break

print("The Sum of ALL elements in an array arr1 is: ", sum_array)

# Simply we can also use the sum method to sum ALL elements in an array
print("The Sum of ALL elements in an array arr1 using sum method is: ", sum(arr1))

# Maximum of ALL elements in an array
print("The Maximum of ALL elements in an array arr1 is: ", max(arr1))

# Sorted elements of an array in ascending order
print("The Sorted elements in an array arr1 using sort method is: ", sort(arr1))

# Trigonometric operations using Numpy
# Sine operation
print("The sine values of arr1 are: " ,sin(arr1))

# Cosine operation
print("The cosine values of arr1 are: " ,cos(arr1))

# Tan operation
print("The tangent values of arr1 are: " ,tan(arr1))

# log values (with base e)
print("The log values of arr1 are: " ,log(arr1))

# square root (here we are using numpy library instead of math library)
print("The square root values of arr1 are: " ,sqrt(arr1))
