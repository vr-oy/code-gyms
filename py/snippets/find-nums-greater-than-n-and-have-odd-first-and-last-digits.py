# Define a function named 'test' that takes a list of numbers as input
# The function filters numbers greater than n with odd first and last digits
def test(nums):
    # Use a list comprehension to filter numbers based on specified conditions
    return [x for x in nums if x > n and x % n % 2 and int(str(x)[0]) % 2]

# Create a list of numbers named 'nums'
n:int = int(input('Enter the exclusive minimum value :'))
list_str:str = input('Enter the comma separated numbers:')
if(not list_str or not all(map(lambda item : item.isnumeric(),list_str.split(',')))):
    print('the input is invalid')
else:
    # Create a list 'nums' with specific elements
    nums = list(map(int,list_str.split(',')))
    
# Print a message indicating the task and the original list of numbers
print("Original list of numbers:")
# Print the original list of numbers
print(nums)
# Print a message indicating the task and the result of the test function applied to 'nums'
print("Numbers of the said array that are greater than n and have odd first and last digits:")
# Print the result of the test function applied to 'nums'
print(test(nums))
