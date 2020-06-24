# Program to find the factorial of a given number without recursion

def fact_without_recursion(n):
    f = 1

    # start range from 1 since we have multiplication, otherwise result will be 0
    for i in range(1, n + 1):
        f = f * i

    return f

# Store the return value f of the function fact_without_recursion in final_result
final_result= fact_without_recursion(int(input("Enter the factorial number to calculate: ")))

print(final_result)
