#Swapping numbers using a third temp variable
# a = 2
# b = 3

#Taking values via user input
#input() function will output a string
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

#Printing to check the return data type, the return should be an integer not a string.
print("The return types of a and b are", type(a), type(b))

temp = a
a = b
b = temp 

print("The values of a and b after swapping using a third temp variable are", a,b)
