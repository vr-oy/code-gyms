# Import the 'zip_longest,' 'chain,' and 'tee' functions from the 'itertools' module
from itertools import zip_longest, chain, tee

# Define a function named 'replace2copy' that takes a list 'lst' as input and returns a new list with elements rearranged
def replace2copy(lst):
    # Use the 'tee' function to create two independent iterators from 'lst'
    lst1, lst2 = tee(iter(lst), 2)

    # Use 'zip_longest' to pair elements from 'lst' with an offset to create a new sequence
    # Chain the pairs together and convert them to a list
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

# Define a list 'n' containing numeric elements
n = [0, 1, 2, 3, 4, 5]

# Call the 'replace2copy' function with 'n' as the argument and print the result
print(replace2copy(n))
