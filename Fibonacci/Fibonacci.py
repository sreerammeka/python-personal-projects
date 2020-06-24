# Program for Fibonacci sequence
# Fibonacci sequence has the following pattern: 0 1 1 2 3 5 8 13 21 which has a pattern
# Add first number and second number results to third number, Add second number and third number results to fourth number

# Pattern is add and shift numbers to the right and continue this process till n-1 values

n= int(input("Enter the maximum values for the Fibonacci sequence: "))

# Initializing first two values
a = 0
b = 1

print(a)
print(b)

def fibonacci(n):
    # Since we already know first two values: 0 and 1, start from 2 and end till n-1 since we are using range
    global a,b
    for i in range(2, n):
        c = a + b
        # swapping numbers which shift a and b variables to the right
        a = b
        b = c
    print(c)


fibonacci(n)
