# Define a function named 'test' that takes a list 'li' and an integer 'i' as input
def test(li, i):
    # Check if the sum of the first 'i' integers in 'li' equals 'i'
    return sum(li[:i]) == i

count:int = int(input('Enter the count of numbers to check:'))
list_str:str = input('Enter the comma separated numbers:')

if(not list_str or not all(map(lambda item : item.isnumeric(),list_str.split(',')))):
    print('the input is invalid')
elif( len(list_str) < count):
    print('count should not be more than the length of numbers provided')
else:
    # Create a list 'nums' with specific elements
    nums = list(map(int,list_str.split(',')))
    
    result = test(nums, count)
    
    print('Result: %s' % result)
