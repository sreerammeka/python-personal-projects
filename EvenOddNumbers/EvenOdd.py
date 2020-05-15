# Python program to print odd or even numbers
# Note: If we input a number, still it takes the input as string (so we need to convert string to int)


#Input function returns a string
a = int(input("Enter a value"))


#Can either check if entered value is a string or not by: 1) Either checking entered input value is a string 2) Or check if entered input value is not an integer
# if type(a) != int:
# if a is not int:

# if type(a) == str:
#     print("The entered value is a character not a number")

#Calculating a remainder value for given input and checking remainder value is 0 or not
#Also testing if input is even or odd, then check if input is greater than 6
if a % 2 == 0:
    print("The entered value is Even number")
    if a > 6:
        print("The number entered is greater than 6")
    else:
        print("The number entered is NOT greater than 6")
else:
    print("The entered value is Odd number")
    if a > 6:
        print("The number entered is greater than 6")
    else:
        print("The number entered is NOT greater than 6")

#Testing first if a entered value is greater than 6, then check even or odd, then print accordingly
# if a > 6:
#     print("The number entered is greater than 6")
#     if a % 2 == 0:
#         print("The entered value is Even number and greater than 6")
#     else:
#         print("The entered value is Odd number and greater than 6")
# else:
#     print("The number entered is NOT greater than 6")
#     if a % 2 == 0:
#         print("The entered value is Even number and NOT greater than 6")
#     else:
#         print("The entered value is Odd number and NOT greater than 6")

