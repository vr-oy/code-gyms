from ..utils.input_utils import Input_Utils

# Define a function named 'test' that takes a list 'li' and an integer 'i' as input
def test(li, i):
    # Check if the sum of the first 'i' integers in 'li' equals 'i'
    return sum(li[:i]) == i

count:int = int(input('Enter the count of numbers to check:'))

nums = Input_Utils.get_number_list_interactively()

print('does the sum of first n number equal n? : ', test(nums, count))
