# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    total = 0  # Start with zero
    while number > 0:
        digit = number % 10  # Get the last digit
        total =total + digit       # Add it to the total
        number = number // 10  # Remove the last digit

    return total

# Example usage
print(sum_of_digits(1234))  # Output: 10 (1+2+3+4)
