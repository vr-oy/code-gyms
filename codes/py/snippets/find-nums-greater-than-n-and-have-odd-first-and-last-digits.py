from ..utils.input_utils import Input_Utils

# Define a function named 'test' that takes a list of numbers as input
# The function filters numbers greater than n with odd first and last digits
def test(nums):
    # Use a list comprehension to filter numbers based on specified conditions
    return [x for x in nums if x > n and x % 2 and int(str(x)[0]) % 2]

# Create a list of numbers named 'nums'
n:int = int(input('Enter the exclusive minimum value :'))

nums = Input_Utils.get_number_list_interactively()

# Print a message indicating the task and the result of the test function applied to 'nums'
print("Numbers of the said array that are greater than n and have odd first and last digits:")
# Print the result of the test function applied to 'nums'
print(test(nums))
