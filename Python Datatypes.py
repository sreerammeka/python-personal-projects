#Different data types in Python

None (same as null in Java or other languages)
Numeric (int, float, complex (2+4j), bool)
list
tuple
set
string (denoted as str)
range
dictionary (or map, map is also a dictionary)

#complex numbers
#Returns a complex variable c = 2+4j
c = complex(2,4)

#Boolean values
#Will return "False" since a is NOT > b
#True is denoted as 1 and FALSE as 0
a = 1
b = 10
c = a > b 

# range
# Use range to only take even or odd numbers
# range(starting_value, ending_before_value, difference)
#even numbers using range
range(2, 10, 2) will output [2, 4, 6, 8]
#even numbers using range
range(1, 10, 2) will output [1, 3, 5, 7, 9]

range(2, 10, 3) will output [2, 5, 8]?