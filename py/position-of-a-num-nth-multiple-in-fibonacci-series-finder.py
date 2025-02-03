# Recursive function to find the nth number in the Fibonacci series
def fib(n, memo):
    if n == 1 or n == 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Function to find the nth multiple of k in the Fibonacci series
def fib_multiple(k, n):
    memo = [0] * 100
    count = 0
    for i in range(1, 100):
        if fib(i, memo) % k == 0:
            count += 1
            if count == n:
                return i
    return -1

# Test the function with sample inputs
k = 2
n = 3
result = fib_multiple(k, n)
print(f"The {n}th multiple of {k} in the Fibonacci series is at position {result}")

k = 4
n = 5
result = fib_multiple(k, n)
print(f"The {n}th multiple of {k} in the Fibonacci series is at position {result}")
