# License: https://bit.ly/3oLErEI

from ..utils.input_utils import Input_Utils

arr_len = 8
nth = 4
count = 3

# Define a function named 'test' that takes a list 'nums' as input
def test(nums):
    # Check if the length of 'nums' is 8 and the count of the fifth element in 'nums' is equal to 3
    return len(nums) == arr_len and nums.count(nums[nth]) == count

nums = Input_Utils.get_number_list_interactively()

# Print the result of the test function applied to the modified 'nums' list
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))
