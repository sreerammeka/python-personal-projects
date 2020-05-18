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
# Nested while loops
while x < 5:
    # Specifying "end" will ensure that it will be on same line
    print("Hello, testing a while loop ", end="")
    y = 0
    while y < 3:
        print("Nested while loop ", end="")
        y+= 1
    # incrementing the value of x, otherwise x will remain the same and will be stuck in a loop
    x+= 1
    # prints on a new line
    print()


#for loop
# for loop can be used to index elements in equences, i.e list, tuple, set, string etc one at a time

a = ["Hello", 2.5, 3]
b= "World"

# The first for loop will index "Hello" first, then goes to second for loop and index each element separately "W", "o", "r", "l", "d",
# then index the value 2.5 from first for loop, then index "W", "o", "r", "l", "d" from the second loop
# then index the value  from first for loop, then index "W", "o", "r", "l", "d" from the second loop
for i in a:
    print(i)
    # print(i, end=" ")

    # This for loop will index each element in string one by one
    for j in b:
        print(j)
        # for p in range(2,10,2):
        # start from 11 and end before 20 with increment 2 in increasing order
        for p in range(11, 20, 2):
            print(p)

            # print the values in decreasing order starting from 10 and ending with 1
            for q in range(10,0,-1):
                print(q)

# break, continue, pass
# break statement will be used to break out of a loop and halt remaining execution
# continue statement will be used to skip execution but not break out of the loop
# pass statement will pass the execution even though nothing is performed. It will skip the block
