# Filter Map Reduce

# Filter- Filter is used to filter values from so many values i.e finding even or odd numbers from a list of values

# Map- Map is used when we want to change ALL values in a list and perform some operation such as add new number to them
# multiply the numbers by 2 etc

# Reduce- Reduce to a single value from a list of values, add ALL values in a list and output one value

# **Filter is only used to filter values but can't modify the values whereas map is used to perform some operation i.e modify values, reduce if we want to reduce to a single final value

# Syntax is
# filter(function_name, list_name)
# filter outputs a sequence not a list, so we need to convert to list

# map(function_name, list_name)
# map performs some operation and outputs a sequence not a list, so we need to convert to list

# reduce(function_name, list_name)
# reduce performs some operation and outputs a single value, so a list is not needed

# In order to use "reduce", we need to import functools library
from functools import reduce

num_list = [22, 15, 17, 31, 19, 24, 34]


# Function is_even returns True if number is even
def is_even(n):
    return n % 2 == 0


def update_values(n):
    return n * 2


# Filters values on the num_list based on the function operation. If the number is even, then store those values
# Then we need to convert those values to a list and store the list values in even_list
even_list_with_function = list(filter(is_even, num_list))

even_list_with_lambda = list(filter(lambda n: n % 2 == 0, num_list))

#
double_list_with_function = list(map(update_values, even_list_with_function))

# Using map to modify the values from the even_list_with_lambda list
double_list_with_lambda = list(map(lambda n: n * 2, even_list_with_lambda))

# If we want to add ALL the values in a list to a final value, then we need to add two values at a time
# Here we are using a lambda and passing two input arguments a and b
# We are saying a+b, we can also reduce to a final value by performing the operation a * b
reduced_value = reduce(lambda a, b: a + b, double_list_with_lambda)

print("List of even numbers using a function: ", even_list_with_function)
print("List of even numbers using a lambda: ", even_list_with_lambda)

print("Doubling the list of numbers using a map function with function list: ", double_list_with_function)
print("Doubling the list of numbers using a map function with lambda: ", double_list_with_lambda)
print("The final reduced value is: ", reduced_value)
