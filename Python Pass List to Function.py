# Pass a list as input to a function and return even and odd numbers

# manual input
# list1 = [10, 22, 31, 42, 25]

# Taking user input through list comprehension
list1 = list(j for j in input("Enter the list of numbers:").strip().split())[:n]

def func_even_odd(list1):
    global even
    even = 0
    global odd
    odd = 0
    for i in list1:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


func_even_odd(list1)

# If we don't use global keywords, then use assign the values for even and odd as below
# even, odd = func_even_odd(list1)

# Passing values inside a print function using format option
# format is a string, so it passes the arguments inside it accordingly
print("Even: {} and Odd: {}".format(even, odd))
