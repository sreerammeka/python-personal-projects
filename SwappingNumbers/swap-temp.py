#Swapping numbers using a third temp variable
#Testing with predefined input
# a = 2
# b = 3

#Taking values via user input
#input() function will output a string, so convert to integers using int()
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

#Printing to check the return data type, the return should be an integer not a string.
print("The return types of a and b are", type(a), type(b))

#A function for swapping two variables, works for both numbers and alphabets
#Functions are used to perform the same set of operations mutiple times without defining them for multiple inputs
def swapping(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print("The values of a and b after swapping using a third temp variable are", swapping(a,b))

#Testing if we can swap two alphabets, here we can only enter alphabets instead of numbers, input() returns a string only
p = input("Enter the value of p")
q = input("Enter the value of q")

print("The values of p and q after swapping using a third temp variable are", swapping(p,q))