# Define a function named 'test' that takes a dictionary of character counts as input
def test(counts):
    # Use a nested loop to generate a string with characters repeated according to their counts
    return " ".join(c for c, i in counts.items() for _ in range(i))

# Example 1
strs1 = {"f": 1, "o": 2}
print("Original string:", strs1)
print("String consisting of space-separated characters with given counts:")
print(test(strs1))

# Example 2
strs2 = {"a": 1, "b": 1, "c": 1}
print("\nOriginal string:", strs2)
print("String consisting of space-separated characters with given counts:")
print(test(strs2))
