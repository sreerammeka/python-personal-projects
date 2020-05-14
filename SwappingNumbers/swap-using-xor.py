#Swapping numbers without using a third temp variable and saving spaces for bits (i.e 11 requires 4 binary digits)
#Use XOR as it uses bit by bit operation


a = 5
b = 6

a = a ^ b
b = a ^ b
a = a ^ b

print("The values of a and b using a third temp variable and spacing space is", a,b)