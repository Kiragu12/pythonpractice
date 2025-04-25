# Function to check if a number is even or odd
def checkevenorodd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# testing
print(checkevenorodd(5))  # Output: Odd
print(checkevenorodd(1))  # Output: Even
