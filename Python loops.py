#loops and iterations in python
#To debug, set a breakpoint after input, press debug and press F8, watch the values in the debugger window
x = int(input("Enter a value:"))

# if elif else
if x > 5:
    print("IF statement executes and outputs TRUE, so will ignore other ELIF and ELSE statements")
elif x < 5:
    print("ELIF means ELSE IF, means it executes ONLY if IF statement fails or other ELIF statements above fails. We use ELIF if multiple statements are to be evaluated")
elif x == 5:
    print("Executes only if above ELIF statement is not executed")
else:
    print("Will execute if both IF and ELIF fails")

#while loop
#While loop is used for doing the same operation multiple times without writing multiple statements
# While can be used for printing on multiple lines
# While executes or performs the operation as long as it fails
# For while loop, 3 things are necessary: initialization, condition, increment or decrement

while x < 5:
    # Specifying end will ensure that it will be on same line
    print("Hello, testing a while loop ", end="")
    y = 0
    while y < 3:
        print("Nested while loop ", end="")
        y+= 1
    x+= 1
    # prints on a new line
    print()


#for loop