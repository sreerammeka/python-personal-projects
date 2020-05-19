# Matrix is ndarray which can be created using the Numpy library
# A matrix in nothing but a combination of one dimensional (1D) arrays

from numpy import *

# In simple terms, We can index an array like a list because an array is a list but with the same datatype instead of
# multiple datatypes

arr1 = array([
    [2,4,5,6,10,9],
    [5,6,7,11,12,13]
], int)

# Convert a 2D array to a 1D array
arr2 = arr1.flatten()

# Printing the matrix
print("The matrix is: ", arr1)

# Print the first 1D array in the matrix arr1
print("The first 1D array in the matrix arr1 is: ", arr1[0])

# Print the second 1D array in the matrix arr1
print("The second 1D array in the matrix arr1 is: ", arr1[1])

# Print the first value from the first 1D array in the matrix arr1
# Prints 2
print("The first value from the first 1D array in the matrix arr1 is: ", arr1[0][0])

# Print the first value from the second 1D array in the matrix arr1
# Prints 5
print("The first value from the first 1D array in the matrix arr1 is: ", arr1[1][0])

# Print the second value from the second 1D array in the matrix arr1
# Prints 6
print("The first value from the first 1D array in the matrix arr1 is: ", arr1[1][1])

# Print the datatype of the array created with Numpy library
# Returns int32 datatype, which means 32 bit integer?
# Numpy arrays will return a 32 bit datatype, it can be 32 bit integer datatype
print("The datatype of array arr1 is: ", arr1.dtype)

# Print the number of dimensions of the ndarray i.e total number of 1D arrays
print("The dimensions of array arr1 is: ", arr1.ndim)

# Print the number of rows and columns in a matrix
# Prints (2,3) which means 2 rows and 3 columns
print("The number of rows and columns respectively in a matrix is: ", arr1.shape)

# Print the size of the matrix..i.e the total number of elements in all the 1D arrays or all dimensions
print("The size of the matrix is : ", arr1.size)

# Convert a multi-dimensional array (here 2D array) to a one dimensional array with all the elements in to a 1D array
# Use flatten() method
print("A one dimensional array from a multi-dimensional 2D array or a matrix is : ", arr1.flatten())

# Convert a multi-dimensional array (here 2D array) to a one dimensional array with all the elements in to a 1D array
# Use reshape(number_of_2D_arrays, number_of_1D_arrays, number_of_values_in_1D_array) method
# Here 2 2D arrays, 2 1D arrays, 3 values in each 1D array
# Converting a 1D array arr2 to a 3D array
print("A one dimensional array from a multi-dimensional 3D array or a matrix is : ", arr2.reshape(2, 2, 3))

# Create a matrix using the matrix() method
# NOT RECOMMMENDED: Python 3.7 says matrix(arr1) is not a recommended way of creating a matrix.It says to use multiple ndarrays
m = matrix(arr1)
print("The matrix created using matrix method is: ", m)

# Print the diagonal elements in a matrix m
# Currently prints diagonal elements [2,6], needs more diagonal elements in matrix m
print("The diagonal elements in a matrix is: ", diagonal(m))

# Print the minimum value in a matrix
print("the minimum value in a matrix is: ", m.min())

# Print the maximum value in a matrix
print("the maximum value in a matrix is: ", m.max())