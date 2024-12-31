# Define a function named 'test' that takes a list of lists of numbers 'nums' as input
def test(nums):
    # Use a list comprehension to check if the sum of each triple in 'nums' is equal to zero
    return [sum(t) == 0 for t in nums]

# Assign a specific list of lists 'nums' to the variable
nums = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]

# Print a message indicating the original list of lists
print("Original list of lists:", nums)

# Print a message indicating the operation to be performed
print("Determine which triples sum to zero:")
# Print the result of the test function applied to 'nums'
print(test(nums))

# Assign another specific list of lists 'nums' to the variable
nums = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]

# Print a message indicating the original list of lists
print("\nOriginal list of lists:", nums)

# Print a message indicating the operation to be performed
print("Determine which triples sum to zero:")
# Print the result of the test function applied to 'nums'
print(test(nums))
