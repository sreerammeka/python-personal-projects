#Taking user input via the python command line, i.e it won't execute on IDE.
#This is written for testing execution on command line ONLY
#For this, we have to use argv which means argument values
#argv uses a list, so indexing is used to pass values passed via the command line
# argv = [<file_name>, <input1>, <input2>, ...]

#For argv, sys module should be imported
#Importing sys module
import sys

#Normal Execution of Python file is:
#python <file_name>
#Here <file_name> is argv[0]

#Execution of Python file on command line with user input in the same line is:
#The below example is a sample for two inputs
#python <file_name> <input1> <input2>
#Here <file_name> is argv[0], <input1> is argv[1], <input2> is argv[2]

#Testing by adding two numbers given with user input
a = int(sys.argv[1])
b = int(sys.argv[2])

c = a + b
print(c)