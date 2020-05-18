# Printing patterns
# Implementing the same patterns using for and while loop
# Print the below pattern:
# # # #
# # # #
# # # #
# # # #

print("for loop started")
# Here we are printing # 1 time using first for loop, and remaining # on the same line using second for loop (Instead we can use the first for loop for line index and print all # using the second for loop)
for i in range(4):
    print("# ", end="")
    for j in range(3):
        print("# ", end="")

    print()

print(
    "pattern printing without printing first # using first for loop and instead use second for loop for printing pattern")
for i in range(4):
    for j in range(4):
        print("# ", end="")

    print()

print("for loop ended, while loop started")
x = 1
y = 1
while x <= 4:
    print("# ", end="")
    y = 1
    while y <= 3:
        print("# ", end="")
        y += 1
    x += 1
    print()

print("printing the same pattern using for and while loop")

z = 1
for i in range(4):
    z=1
    while z <= 4:
        print("# ", end="")
        z += 1

    print()
