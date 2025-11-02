
# factorial_program.py

def factorial(n):
    """Calculate factorial of a number using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number
number = 5
result = factorial(number)

print(f"The factorial of {number} is: {result}")
def factorial(n):
    """Calculate factorial of a number using a loop"""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example call
number = 5
print(f"The factorial of {number} is: {factorial(number)}")
