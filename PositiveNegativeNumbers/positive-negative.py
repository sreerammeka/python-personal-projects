# Python program to check if given input is positive or negative

a = bin(int(input("Enter a number")))
print(type(a))

if a[0] == "-":
    print("The number entered is a negative number", a)
else:
    print("The number entered is a positive number", a)


