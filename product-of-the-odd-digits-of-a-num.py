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
n = 123456789

# Print a message indicating the operation to be performed
print("Original Number:", n)

# Print a message indicating the operation to be performed
print("Product of the odd digits in the said number, or 0 if there aren't any:")
# Print the result of the test function applied to 'n'
print(test(n))

# Assign another specific integer 'n' to the variable
n = 2468

# Print a message indicating the operation to be performed
print("\nOriginal Number:", n)

# Print a message indicating the operation to be performed
print("Product of the odd digits in the said number, or 0 if there aren't any:")
# Print the result of the test function applied to 'n'
print(test(n))

# Assign another specific integer 'n' to the variable
n = 13579

# Print a message indicating the operation to be performed
print("\nOriginal Number:", n)

# Print a message indicating the operation to be performed
print("Product of the odd digits in the said number, or 0 if there aren't any:")
# Print the result of the test function applied to 'n'
print(test(n))
