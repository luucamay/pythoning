'''
Recursive Multiply - Cracking the coding interview
Chapter 8, Problem #5

Write a recursive function to multiply two positive integers without using the * operator.
You can use addition, substraction, and bit shifting, but you should minimize the number of these operations.

Hints: #166, #203, #227, #234, #246, #280
'''
# Approach 1
def multiply(a, b):
    if a == 0:
        return 0
    return b + multiply(a -1, b)
# Test
print multiply(8,7)
# Approach 2
def min_product(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return min_product_helper(smaller, bigger)

def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1 # divide by 2
    half_prod = min_product_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod
    return half_prod + half_prod + bigger
# Test
print min_product(4, 5)
