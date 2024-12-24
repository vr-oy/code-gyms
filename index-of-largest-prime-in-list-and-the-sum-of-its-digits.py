# Define a function named 'test' that takes a list of numbers as input
def test(nums):
    # Find the maximum prime number in the list along with its index
    n, i = max((n, i) for i, n in enumerate(nums) if is_prime(n))
    
    # Return a list containing the index of the largest prime and the sum of its digits
    return [i, sum(int(c) for c in str(n))]

# Define a function named 'is_prime' that checks if a number is prime
def is_prime(n):
    return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

# Example 1
nums1 = [3, 7, 4]
print("List of numbers:", nums1)
print("Index of the largest prime in the said list and the sum of its digits:")
print(test(nums1))

# Example 2
nums2 = [3, 11, 7, 17, 19, 4]
print("\nList of numbers:", nums2)
print("Index of the largest prime in the said list and the sum of its digits:")
print(test(nums2))

# Example 3
nums3 = [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
print("\nList of numbers:", nums3)
print("Index of the largest prime in the said list and the sum of its digits:")
print(test(nums3))
