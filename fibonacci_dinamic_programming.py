def fibonacci(n):
    return fibonacci_helper(n, [0]*(n+1))

def fibonacci_helper(i, memo):
    if i == 0 or i == 1:
        return i
    if not memo[i]:
        memo[i] = fibonacci_helper(i-1, memo) + fibonacci_helper(i-2, memo)
    return memo[i]

# Test
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)

