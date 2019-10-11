def fibonacci(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return a + b

# Test
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)
print fibonacci(6)
