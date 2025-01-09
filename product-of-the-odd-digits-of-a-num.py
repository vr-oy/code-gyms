# Define a function named 'test' that takes an integer 'n' as input
def test(n):
    # Check if any digit in the number is odd
    if any(int(c) % 2 for c in str(n)):
        
        # Initialize a variable 'prod' to store the product of odd digits
        prod = 1
        
        # Iterate over each digit in the number
        for c in str(n):
            # If the digit is odd, multiply it with the current product
            if int(c) % 2 == 1:
                prod *= int(c)
        # Return the final product of odd digits
        return prod
    # Return 0 if there are no odd digits in the number
    return 0

# Assign a specific integer 'n' to the variable
n = int(input('Enter the number:'))

print("\nProduct of the odd digits in the said number, or 0 if there aren't any:")

print(test(n))
