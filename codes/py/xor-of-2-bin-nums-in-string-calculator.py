
def test(nums):
    # Use binary XOR (^) on the integers converted from the binary strings in the input list
    # Convert the result back to a binary string
    return bin(int(nums[0], 2) ^ int(nums[1], 2))


# Assign a specific list of side lengths 'sides' to the variable
nums = input("Enter the comma separated binary numbers:")

nums = nums.split(',')

# Print the original list of binary strings 'nums'
print("The provided binary numbers are:")
print(nums)

# Print a message indicating the operation to be performed
print("XOR of two said strings interpreted as binary numbers:")

# Print the result of the test function applied to the 'nums' list
print(test(nums))
