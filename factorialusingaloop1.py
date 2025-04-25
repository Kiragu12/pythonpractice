# Function to compute factorial using a loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result =result * i
    return result

# Example usage
print (factorial_loop(5))  # Output: 120
