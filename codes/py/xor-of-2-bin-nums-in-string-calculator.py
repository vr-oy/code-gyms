# Define a function named 'test' that takes a list of binary strings 'nums' as input
def test(nums):
    # Use binary XOR (^) on the integers converted from the binary strings in the input list
    # Convert the result back to a binary string
    return bin(int(nums[0], 2) ^ int(nums[1], 2))

# Assign a specific list of binary strings 'nums' to the variable
nums = ["0001", "1011"]

# Print the original list of binary strings 'nums'
print("Original strings:")
print(nums)

# Print a message indicating the operation to be performed
print("XOR of two said strings interpreted as binary numbers:")

# Print the result of the test function applied to the 'nums' list
print(test(nums))

# Assign a different list of binary strings 'nums' to the variable
nums = ["100011101100001", "100101100101110"]

# Print the original list of binary strings 'nums'
print("\nOriginal strings:")
print(nums)

# Print a message indicating the operation to be performed
print("XOR of two said strings interpreted as binary numbers:")

# Print the result of the test function applied to the updated 'nums' list
print(test(nums))
