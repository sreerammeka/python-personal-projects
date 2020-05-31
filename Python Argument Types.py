# Types of Arguments in Python
# 1. Formal Arguments - arguments passed when defining a function such as a,b in add(a,b)
# 2. Actual Arguments - values passed when defining a function such as 3,4 in add(3,4)

# There are 4 types of Actual Arguments:
# 1. Position
# 2. Keyword
# 3. Default
# 4. Variable Length

# Position Argument Example
def person_details(name, age):
    print(name)
    print(age)


# Here values "sunil" and 35 are passed to arguments "name" and "age" respectively. So values are passed to arguments
# using position
person_details("sunil", 35)

# The number of input arguments passed when defining a function must be passed when calling the function,
# Otherwise, it will throw an error
# person_details("sunil") will throw an error as it requires 2 arguments but we are passing only one argument

# Keyword Argument Example
# If we don't know the position the values are passed to a function, then we can use the keyword arguments "name" and
# "age" and assign values in any order but it will pass the values taking the keyword into consideration
person_details(age=43, name="John")


# Default Argument Example
# Default values are specified inside the function arguments
# Here if age is not modified anywhere, then the default value of age is 28 when referenced in the program
def person_details1(name, age=28):
    print(name)
    print(age)


# Here, the default values is being modified by passing new value 35, so age will get 35
person_details1("sunil", 35)


# **Variable Length Argument Example
# Here argument "a" is mandatory and can have one value. If we don't know how many values will be passed as we can't
# pass 100 arguments for 100 values, we use *b to denote the argument "b" can take multiple values
# We use this if we don't know the number of values that will be provided
# The values in b will be stored as a tuple

def sum(a, *b):
    c = a
    print("The value of a is :", a)
    print("The value of b is :", b)
    for i in b:
        c = c + i
    print("The sum when taking one input a as mandatory input and other input b as variable length argument is :", c)


# a will store the first mandatory fixed value 2, b will store a tuple (3, 5, 6) since it can have multiple values
sum(2, 3, 5, 6)


# We can improve the above function by passing all values to b instead of storing one value in a and others in b
def sum_optimized(*b):
    c = 0
    print("The value of b is :", b)
    for i in b:
        c = c + i
    print("The sum when taking one input b as variable length argument is :", c)


# b will store a tuple (2, 3, 5, 6) since it can have any number of values
sum_optimized(2, 3, 5, 6)


# We can use variable length arguments on integers, strings, float etc
# on tuples, list (need to check and verify)

# Taking the name argument as variable length argument and passing strings as input
# name will store a tuple ('sunil', 'john', 'michael')
def person_name(*name):
    print("The names are :", name)
    for i in name:
        print(i)


person_name("sunil", "john", "michael")


# We can't pass values to variable length arguments *data directly with keywords such as age, phone_num, city etc
# To avoid this issue, we have to use "Keyworded Variable Length Arguments" using **data or **kwargs,
# also called keyword arguments in short
# "Keyworded Variable Length Arguments" will store as a "dictionary" instead of like a "tuple" in "Variable Length Arguments"
def person(name, **data):
    # passes name = sunil and prints "sunil" and the other keywords arguments as a "dictionary"
    print("The name is ", name)
    print("The values stored in data as dictionary is ", data)

    # Index a key and value each time using the below for loop. Index the key using "key or i", value using "value or j"
    # A dictionary can be indexed by calling dictionary_name.items() which displays keys and values
    # i is indexing a key, j is indexing a value

    # Indexing both key and value from the key, value pairs in the dictionary "data"
    for i, j in data.items():
    # for key, value in data.items():
        # prints key and value side by side
        print("The key and value in the dictionary data is :", i, j)

    # Indexing both key and value from the key, value pairs in the dictionary "data" but printing only "value"
    for i, j in data.items():
    # for key, value in data.items():
        print("The values in the dictionary data is :", j)

    # Indexing both key and value from the key, value pairs in the dictionary "data" but printing only "keys"
    for i, j in data.items():
    # for key, value in data.items():
        print("The keys in the dictionary data is :", i)

    # Indexing both key and value from the key, value pairs in the dictionary "data" but printing both "key" and "value"
    # Here i is indexing both key and value
    for i in data.items():
    # for key, value in data.items():
        print("The key and value pair in the dictionary data is :", i)

    # Indexing both key and value from the key, value pairs in the dictionary "data" but printing both "key" and "value"
    # as a tuple because it is indexing both key and value
    # Here i is indexing both key and value
    # Even though j is not indexed, j will take the last value in previous for loop which is "Hyderabad"
    for i in data.items():
    # for key, value in data.items():
        print("The key and value pair in the dictionary data is :", i, j)

person("sunil", age=35, phone_num=456789, city="Hyderabad")
