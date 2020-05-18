# Python arrays
# Arrays are used to store the same type of data (i.e same datatype) in an efficient way.
# Mostly they are used to store large amounts of data

# Example to ask the user for data as input and add to an empty array

# Library for using arrays
# import array
# We can also import a module using this, this will help in less typing
from array import *

# Array syntax
# Typecode means datatype
# array('typecode',[1,2,3,4])
# An empty array of integer datatype
arr = array('i', [])

n = int(input("Enter the number of values to be added to the array:"))

for i in range(n):
    # Take the input from the user everytime
    x = int(input("Enter the next value to add to the array:"))
    # Append data to the array each time after storing the value into x
    arr.append(x)

# Note: You can't directly print the value using print(arr.append(x)) because it returns None
# You have to print the array directly without the method
print(arr)

# Searching whether a given input from user is present in the array or not
# Else can also be used with "for" loop NOT only with "IF" statement
val = int(input("Enter a value to search:"))
# counter = 0
# for j in arr:
#     if j == val:
#         # Printing the index value
#         print(counter)
#         # Break out of the loop if value matches with the value entered by user, otherwise continue the search
#         break
#     counter += 1
# else:
#     print("The entered input value is not present in the array")

# Alternatively, instead of using a for loop and if loop, we can use built in method of array "index"
# Here value of val will be searched in the array, then will print the index if it matches, otherwise will output ValueError

# print(arr.index(val))
# Try and except, else
# Try executing this block, if error found then return error using except, or print the error to the user in the except block
try:
    print(arr.index(val))
# Catching the ValueError exception
# If exceptions are present after the try block is executed, then use the exceptions block to catch those specific exceptions
except ValueError as v:
    print("The entered value to search is not present in the array. The error is: ", v)
# Else do this, if no exception or error is found
else:
    print("There are no exceptions found")


