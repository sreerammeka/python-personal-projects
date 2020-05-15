#loops and iterations in python
x = int(input("Enter a value:"))
if x > 5:
    print("IF statement executes and outputs TRUE, so will ignore other ELIF and ELSE statements")
elif x < 5:
    print("ELIF means ELSE IF, means it executes ONLY if IF statement fails or other ELIF statements above fails. We use ELIF if multiple statements are to be evaluated")
elif x == 5:
    print("Executes only if above ELIF statement is not executed")
else:
    print("Will execute if both IF and ELIF fails")

