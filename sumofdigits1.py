# Function to compute factorial using recursion
def factorialrecursive(n):
    # Base case factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n - 1)
        return n * factorialrecursive(n - 1)

# Example usage
print(factorialrecursive(9))