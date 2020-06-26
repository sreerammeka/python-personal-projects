# Program to find the factorial of a given number with recursion

result = 1


def factorial_with_recursion(n):
    global result

    if n == 0:
        result = 1
    else:
        result = n * factorial_with_recursion(n - 1)

    return result


final_result = factorial_with_recursion(int(input("Enter the factorial to calculate: ")))

print(final_result)
