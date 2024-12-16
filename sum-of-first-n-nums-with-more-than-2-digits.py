# Define a function named 'test' that takes a list of numbers 'nums' and an integer 'k' as input
def test(nums, k):
    # Initialize a variable 's' to store the sum of numbers meeting the specified conditions
    s = 0
    # Iterate through the first 'k' elements in 'nums'
    for i in range(len(nums))[:k]:
        # Check if the absolute value of the current number has more than 2 digits
        if len(str(abs(nums[i]))) > 2:
            # Add the current number to the sum 's'
            s = s + nums[i]
    # Return the final sum 's'
    return s

# Assign a specific list of numbers 'nums' to the variable
nums = [4, 5, 17, 9, 14, 108, -9, 12, 76]

# Print a message indicating the operation to be performed
print("Original list:", nums)

# Assign a specific value 'K' to the variable
K = 4

# Print a message indicating the value of 'K'
print("Value of K:", K)

# Print a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Print the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# Assign another specific value 'K' to the variable
K = 6

# Print a message indicating the value of 'K'
print("\nOriginal list:", nums)
print("Value of K:", K)

# Print a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Print the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# Assign another specific list of numbers 'nums' to the variable
nums = [114, 215, -117, 119, 14, 108, -9, 12, 76]

# Print a message indicating the operation to be performed
print("\nOriginal list:", nums)

# Assign another specific value 'K' to the variable
K = 5

# Print a message indicating the value of 'K'
print("Value of K:", K)

# Print a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Print the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# Print an additional message indicating the original list
print("\nOriginal list:", nums)

# Assign another specific value 'K' to the variable
K = 1

# Print a message indicating the value of 'K'
print("Value of K:", K)

# Print a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Print the result of the test function applied to 'nums' and 'K'
print(test(nums, K))
