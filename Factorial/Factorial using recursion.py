# Program to find the factorial of a given number with recursion

# To check or set recursion limit beyond 1000, we need to import sys. Default is 1000
import sys

# Change or set the recursion limit
sys.setrecursionlimit(2000)
# Printing the current recursion limit
print("The current recursion limit is: ", sys.getrecursionlimit())


result = 1


def factorial_with_recursion(n):
    # A global variable can be accessed and can't be modified inside a function, so that's why we have to declare
    # using global keyword to modify that variable
    global result

    if n == 0:
        result = 1
    else:
        result = n * factorial_with_recursion(n - 1)

    return result


final_result = factorial_with_recursion(int(input("Enter the factorial to calculate: ")))

print(final_result)


