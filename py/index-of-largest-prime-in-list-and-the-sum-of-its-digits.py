# Define a function named 'test' that takes a list of numbers as input
def test(nums):
    # Find the maximum prime number in the list along with its index
    n, i = max((n, i) for i, n in enumerate(nums) if is_prime(n))
    
    # Return a list containing the index of the largest prime and the sum of its digits
    return [i, sum(int(c) for c in str(n))]

# Define a function named 'is_prime' that checks if a number is prime
def is_prime(n):
    return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

list_str:str = input('Enter the comma separated numbers:')
if(not list_str or not all(map(lambda item : item.isnumeric(),list_str.split(',')))):
    print('the input is invalid')
else:
    # Create a list 'nums' with specific elements
    nums = list(map(int,list_str.split(',')))
        
    print("List of numbers:", nums)
    print("Index of the largest prime in the said list and the sum of its digits:")
    print(test(nums))
