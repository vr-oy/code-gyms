from .utils.input_utils import Input_Utils

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

nums = Input_Utils.get_number_list_interactively()

# Assign a specific value 'K' to the variable
K = int(input("Enter the value of K: "))

# Print a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Print the result of the test function applied to 'nums' and 'K'
print(test(nums, K))
